import json
from collections import defaultdict

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum, F, Q, Prefetch
from decimal import Decimal
import logging
from decimal import Decimal, InvalidOperation, ConversionSyntax

from django.utils.html import escape
from django.views.generic import DeleteView, UpdateView, ListView, CreateView, DetailView
from admin_site.models import SiteSettingModel, ActivityLogModel, SiteInfoModel
from sale.models import SaleModel, SaleItemModel, CustomerModel, CustomerWalletModel, CustomerCrateDebtModel
from inventory.models import ProductModel, CategoryModel, StockInModel

from django.contrib.auth.models import User
from django.utils.timezone import localtime, now
from pytz import timezone as pytz_timezone
from sale.forms import *  # Ensure all forms are imported

# Initialize logger at module level
logger = logging.getLogger(__name__)

try:
    from human_resource.models import StaffModel, StaffProfileModel, StaffWalletModel
except ImportError:
    class StaffModel:
        def __str__(self): return "Dummy Staff"

        @property
        def user(self): return User(username="dummy_user")

    class StaffProfileModel:
        pass

    logger.warning(
        "StaffModel or StaffProfileModel not found in human_resource. Adjust get_staff_instance or import if needed.")


# --- Helper function (ensure this is present and correct for your StaffModel setup) ---
def get_staff_instance(user):
    try:
        return user.profile.staff
    except (AttributeError, StaffProfileModel.DoesNotExist):
        logger.error(f"Staff profile not found for user: {user.username}")
        return None


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = CustomerModel
    permission_required = 'sale.add_customermodel'
    form_class = CustomerForm
    success_message = 'Customer Added Successfully'
    template_name = 'sale/customer/create.html'

    def safe_decimal(self, value_str, default=Decimal('0.00')):
        try:
            val = value_str.strip().replace(',', '') if value_str else ''
            if val == '':
                return default
            return Decimal(val)
        except (ConversionSyntax, InvalidOperation, AttributeError):
            return None

    def get_success_url(self):
        return reverse('customer_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        try:
            with transaction.atomic():
                if self.request.user.is_authenticated:
                    form.instance.created_by = self.request.user

                response = super().form_valid(form)

                current_debt_str = self.request.POST.get('current_debt', '0.00')
                current_debt_decimal = self.safe_decimal(current_debt_str)
                if current_debt_decimal is None or current_debt_decimal < Decimal('0.00'):
                    messages.error(self.request, "Invalid initial debt amount provided. Please enter a valid number.")
                    return self.form_invalid(form)

                customer_wallet, created = CustomerWalletModel.objects.get_or_create(customer=self.object)
                customer_wallet.initial_debt = current_debt_decimal
                customer_wallet.balance = current_debt_decimal
                customer_wallet.save()

                if current_debt_decimal > Decimal('0.00'):
                    messages.info(self.request,
                                  f"Customer wallet initialized with ₦{current_debt_decimal} initial debt.")
                else:
                    messages.info(self.request, "Customer wallet initialized.")

                categories = CategoryModel.objects.all()

                for category in categories:
                    field_name = f'current_empty_debt{category.id}'
                    crate_debt_str = self.request.POST.get(field_name, '0.00')
                    crate_debt_decimal = self.safe_decimal(crate_debt_str)

                    if crate_debt_decimal is None or crate_debt_decimal < Decimal('0.00'):
                        messages.error(self.request,
                                       f"Invalid empty crate debt amount for {category.name}. Please enter a valid number.")
                        return self.form_invalid(form)

                    if crate_debt_decimal > Decimal('0.00'):
                        customer_crate_debt, created = CustomerCrateDebtModel.objects.get_or_create(
                            customer=self.object,
                            category=category
                        )
                        customer_crate_debt.crate = crate_debt_decimal
                        customer_crate_debt.save()
                        messages.info(self.request,
                                      f"Customer owes {crate_debt_decimal} empty crates for {category.name}.")

            return response

        except ValueError as ve:
            messages.error(self.request, f"Customer creation failed: {ve}")
            logger.exception(f"Customer creation failed due to value error: {ve}")
            return self.form_invalid(form)
        except Exception as e:
            messages.error(self.request, f'An unexpected error occurred during customer creation: {e}')
            logger.exception("Customer creation failed due to unexpected error")
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Customer'
        context['category_list'] = CategoryModel.objects.all()
        return context


@login_required
def api_customer_search(request):
    """
    API endpoint for searching customers.
    Filters customers by 'q' (query string) across full_name, mobile, and email.
    Returns customer ID, full_name, mobile, email, current wallet balance,
    and **all associated crate debts by category**.
    """
    query = request.GET.get('q', '').strip()

    customers = CustomerModel.objects.all()

    if query:
        customers = customers.filter(
            Q(full_name__icontains=query) |
            Q(mobile__icontains=query) |
            Q(email__icontains=query)
        )

    customers = customers.select_related('customer_wallet').prefetch_related('crate_debts__category')[:20]

    results = []
    for customer in customers:
        wallet_balance = Decimal('0.00')
        if hasattr(customer, 'customer_wallet'):
            wallet_balance = customer.customer_wallet.balance or Decimal('0.00')

        customer_crate_debts = []
        for crate_debt_instance in customer.crate_debts.all():
            customer_crate_debts.append({
                'category_id': crate_debt_instance.category.id if crate_debt_instance.category else None,
                'category_name': crate_debt_instance.category.name if crate_debt_instance.category else 'N/A',
                'crate_amount': float(crate_debt_instance.crate or Decimal('0.00')),
            })

        results.append({
            'id': customer.id,
            'full_name': customer.full_name,
            'mobile': customer.mobile or '',
            'email': customer.email or '',
            'address': customer.address or '',  # Ensure address is included
            'balance': float(wallet_balance),
            'crate_debts': customer_crate_debts,
        })

    return JsonResponse(results, safe=False)


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CustomerModel
    permission_required = 'sale.view_customermodel'
    template_name = 'sale/customer/index.html'
    context_object_name = "customer_list"

    def get_queryset(self):
        return CustomerModel.objects.all().order_by('full_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Customer List'
        context['form'] = CustomerForm()
        return context


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = CustomerModel
    permission_required = 'sale.view_customermodel'
    template_name = 'sale/customer/detail.html'
    context_object_name = "customer"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Customer Details: {self.object.full_name}'
        context['wallet'] = getattr(self.object, 'customer_wallet', None)
        context['debt_repayment_form'] = CustomerDebtRepaymentForm()
        context['site_setting'] = SiteSettingModel.objects.first()
        context['crate_return_form'] = CustomerCrateReturnForm()
        context['driver_list'] = StaffModel.objects.filter(is_driver=True)
        owed_categories = CategoryModel.objects.filter(
            category_crate_debts__customer=self.object,
            category_crate_debts__crate__gt=0
        ).distinct()
        context['crate_debts'] = CustomerCrateDebtModel.objects.filter(customer=self.object, crate__gt=0).select_related('category')

        context['category_list'] = owed_categories
        context['activity_log_list'] = ActivityLogModel.objects.filter(customer=self.object).order_by('-id')[:20]
        return context


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomerModel
    permission_required = 'sale.add_customermodel'
    form_class = CustomerForm
    success_message = 'Customer Updated Successfully'
    template_name = 'sale/customer/edit.html'

    def get_success_url(self):
        return reverse('customer_detail', kwargs={'pk': self.object.pk})

    def get_initial(self):
        initial = super().get_initial()
        if hasattr(self.object, 'customer_wallet'):
            initial['current_debt'] = self.object.customer_wallet.initial_debt
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Edit Customer: {self.object.full_name}'
        context['category_list'] = CategoryModel.objects.all()
        context['customer_crate_debts'] = self.object.crate_debts.all()
        return context


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CustomerModel
    permission_required = 'sale.delete_customermodel'
    success_message = 'Customer Deleted Successfully'
    template_name = 'sale/customer/delete.html'
    context_object_name = "customer"

    def get_success_url(self):
        return reverse_lazy('customer_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Delete Customer: {self.object.full_name}'
        return context


@transaction.atomic
@login_required
@permission_required("sale.add_customerdebtrepaymentmodel", raise_exception=True)
def customer_debt_repayment_view(request, customer_id):
    customer = get_object_or_404(CustomerModel, pk=customer_id)

    if request.method == 'POST':
        form = CustomerDebtRepaymentForm(request.POST)
        if form.is_valid():
            repayment = form.save(commit=False)
            repayment.customer = customer

            staff_member = get_staff_instance(request.user)
            if not staff_member:
                messages.error(request, "Staff profile not found.")
                return redirect(reverse('customer_detail', kwargs={'pk': customer.pk}))

            repayment.recorded_by = request.user

            wallet, _ = CustomerWalletModel.objects.get_or_create(customer=customer)
            wallet.balance -= repayment.amount_paid
            wallet.save(update_fields=['balance'])

            repayment.balance = wallet.balance
            repayment.save()

            site_setting = SiteSettingModel.objects.first()
            amount = float(repayment.amount_paid)
            driver = None

            if repayment.payment_method == 'cash':
                site_setting.cash_balance = (site_setting.cash_balance or 0.0) + amount
                site_setting.save(update_fields=['cash_balance'])

            elif repayment.payment_method == 'bank':
                site_setting.balance = (site_setting.balance or 0.0) + amount
                site_setting.save(update_fields=['balance'])

            elif repayment.payment_method == 'driver' and repayment.driver:
                driver = repayment.driver
                driver_wallet, _ = StaffWalletModel.objects.get_or_create(staff=repayment.driver)
                driver_wallet.balance += amount
                driver_wallet.save(update_fields=['balance'])

            # --- Activity Log in the same style ---
            staff_url = reverse('staff_detail', kwargs={'pk': staff_member.pk})
            customer_url = reverse('customer_detail', kwargs={'pk': customer.pk})
            timestamp = localtime(repayment.created_at, pytz_timezone('Africa/Lagos')).strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            # Get payment destination display
            if repayment.payment_method == 'driver' and repayment.driver:
                destination_str = f"to driver <b>{escape(repayment.driver.full_name)}</b>"
            elif repayment.payment_method == 'bank':
                destination_str = "to <b>bank</b>"
            else:
                destination_str = "in <b>cash</b>"

            # Compute customer's current debt (wallet.balance represents debt)
            current_debt = wallet.balance

            log_html = f"""
            <div class='bg-success text-white p-2' style='border-radius:5px;'>
              <p>
                <b>
                  <a href="{staff_url}" class="text-white text-decoration-underline">
                    {escape(staff_member.full_name.title())}
                  </a>
                </b>
                recorded a customer repayment of <b>₦{repayment.amount_paid:.2f}</b> {destination_str} for
                <a href="{customer_url}" class="text-white text-decoration-underline">
                  <b>{escape(customer.full_name)}</b>
                </a>.<br>
                <b>Current Debt:</b> ₦{current_debt:.2f}<br>
                <a href="{customer_url}" class="btn btn-sm btn-light mt-2">View Customer</a>
                <span class='float-end'>{timestamp}</span>
              </p>
            </div>
            """

            ActivityLogModel.objects.create(
                log=log_html,
                user=request.user,
                category='sales',
                customer=customer,
                keywords='customer__repayment',
                driver=driver
            )
            # --- End activity log ---

            messages.success(request, f"Repayment of ₦{repayment.amount_paid:.2f} recorded successfully.")
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")

    return redirect(reverse('customer_detail', kwargs={'pk': customer.pk}))

@transaction.atomic
@login_required
@permission_required("sale.add_customerdebtrepaymentmodel", raise_exception=True)
def customer_crate_return_view(request, customer_id):
    customer = get_object_or_404(CustomerModel, pk=customer_id)

    if request.method == 'POST':
        form = CustomerCrateReturnForm(request.POST)
        if form.is_valid():
            refund = form.save(commit=False)
            refund.customer = customer

            staff_member = get_staff_instance(request.user)
            if not staff_member:
                messages.error(request, "Staff profile not found.")
                return redirect(reverse('customer_detail', kwargs={'pk': customer.pk}))

            refund.recorded_by = request.user
            refund.save()

            site_setting = SiteSettingModel.objects.first()
            amount = refund.amount_paid or 0

            # Handle cash returns
            if refund.return_method == 'cash':
                if refund.payment_method == 'cash':
                    site_setting.cash_balance = (site_setting.cash_balance or 0) + float(amount)
                    site_setting.save(update_fields=['cash_balance'])
                elif refund.payment_method == 'bank':
                    site_setting.balance = (site_setting.balance or 0) + float(amount)
                    site_setting.save(update_fields=['balance'])
                elif refund.payment_method == 'driver' and refund.driver:
                    driver_wallet, _ = StaffWalletModel.objects.get_or_create(staff=refund.driver)
                    driver_wallet.balance += float(amount)
                    driver_wallet.save(update_fields=['balance'])

            # Only increment stock for empty returns
            if refund.return_method == 'empty':
                category = refund.category
                category.number_of_empty = (category.number_of_empty or 0) + float(refund.crates_returned)
                category.save(update_fields=['number_of_empty'])

            # Always reduce the customer's crate debt
            ccd, _ = CustomerCrateDebtModel.objects.get_or_create(
                customer=customer,
                category=refund.category
            )
            ccd.crate = max(Decimal('0.00'), ccd.crate - refund.crates_returned)
            ccd.save(update_fields=['crate'])

            # Build activity-log entry
            staff_url    = reverse('staff_detail',    kwargs={'pk': staff_member.pk})
            customer_url = reverse('customer_detail', kwargs={'pk': customer.pk})
            ts           = localtime(refund.created_at, pytz_timezone('Africa/Lagos'))\
                             .strftime("%Y-%m-%d %H:%M:%S")

            # Describe return-method and payment details
            if refund.return_method == 'empty':
                method_str = "<b>Empty Return</b>"
                amt_str    = ""
                dest_str   = ""
            else:  # cash
                method_str = "<b>Cash Return</b>"
                amt_str    = f" and paid <b>₦{amount:.2f}</b>"
                if refund.payment_method == 'driver' and refund.driver:
                    dest_str = f" to driver <b>{escape(refund.driver.full_name)}</b>"
                elif refund.payment_method == 'bank':
                    dest_str = " to <b>bank</b>"
                else:
                    dest_str = ""  # already implied cash

            log_html = f"""
            <div class='bg-success text-white p-2' style='border-radius:5px;'>
              <p>
                <b>
                  <a href="{staff_url}" class="text-white text-decoration-underline">
                    {escape(staff_member.full_name.title())}
                  </a>
                </b>
                recorded a crate return of <b>{refund.crates_returned}</b> empty crates for
                <a href="{customer_url}" class="text-white text-decoration-underline">
                  <b>{escape(customer.full_name)}</b>
                </a>
                as {method_str}{amt_str}{dest_str}.<br>
                <a href="{customer_url}" class="btn btn-sm btn-light mt-2">View Customer</a>
                <span class='float-end'>{ts}</span>
              </p>
            </div>
            """

            ActivityLogModel.objects.create(
                log=log_html,
                user=request.user,
                category='sales',
                customer=customer,
                keywords='customer__crate_return',
                driver=(refund.driver if refund.return_method == 'cash' and refund.payment_method == 'driver' else None)
            )

            # Flash message
            msg = (
                f"Recorded {refund.crates_returned} empty-crate return for '{refund.category.name}' "
                f"({ 'Empty' if refund.return_method=='empty' else f'Cash: ₦{amount:.2f}{dest_str}' })."
            )
            messages.success(request, msg)
        else:
            for field, errors in form.errors.items():
                for err in errors:
                    messages.error(request, f"{field.capitalize()}: {err}")

    return redirect(reverse('customer_detail', kwargs={'pk': customer.pk}))


@login_required
@permission_required("sale.add_salemodel", raise_exception=True)
def sale_create_view(request):
    sale_form = SaleForm()
    formset = SaleItemCreateFormSet(queryset=SaleItemModel.objects.none())
    site_setting = SiteSettingModel.objects.first()

    product_data_for_frontend = {
        str(p.id): {
            'selling_price': float(p.selling_price or 0),
            'quantity': float(p.quantity or 0),
            'cost_price': float(p.last_cost_price or 0),
            'product_type': p.type
        }
        for p in ProductModel.objects.all()
    }
    product_data_for_frontend_json = json.dumps(product_data_for_frontend)
    empty_formset = SaleCategoryEmptyFormSet(prefix='empty_crates')

    if request.method == 'POST':
        sale_form = SaleForm(request.POST)
        formset = SaleItemCreateFormSet(request.POST, queryset=SaleItemModel.objects.none())

        if sale_form.is_valid() and formset.is_valid():

                with transaction.atomic():
                    staff_member = get_staff_instance(request.user)
                    if not staff_member:
                        messages.error(request, "Staff profile not found; cannot record sale.")
                        return redirect(reverse('login'))

                    sale = sale_form.save(commit=False)
                    sale.created_by = request.user
                    sale.save()

                    total_sale_amount = Decimal('0.00')
                    total_discount = Decimal('0.00')
                    saved_items = []

                    for form in formset:
                        if form.cleaned_data.get('DELETE') or not form.cleaned_data.get('product'):
                            continue

                        item = form.save(commit=False)
                        item.sale = sale
                        product = item.product
                        quantity = item.quantity

                        # Confirmed-only inventory logic
                        if sale.status == 'confirmed':
                            quantity_remaining = quantity

                            # Reduce initial_quantity_left
                            if product.initial_quantity_left > 0:
                                qty_used = min(quantity_remaining, Decimal(product.initial_quantity_left))
                                product.initial_quantity_left -= int(qty_used)
                                quantity_remaining -= qty_used
                                product.save(update_fields=['initial_quantity_left'])

                            # FIFO reduction from StockInModel
                            stockins = StockInModel.objects.filter(
                                product=product, status='active', quantity_left__gt=0
                            ).order_by('date_added', 'id')

                            for stock in stockins:
                                if quantity_remaining <= 0:
                                    break
                                consume_qty = min(quantity_remaining, stock.quantity_left)
                                stock.quantity_left -= consume_qty
                                stock.quantity_sold += consume_qty
                                stock.save(update_fields=['quantity_left', 'quantity_sold'])
                                quantity_remaining -= consume_qty
                                item.stock_in = stock  # Last stock used

                            product.quantity = (product.quantity or Decimal('0.00')) - quantity
                            product.save(update_fields=['quantity'])

                        # Always calculate subtotal, profit, discount
                        item.subtotal = item.unit_price * quantity
                        item.cost_price = product.last_cost_price or Decimal('0.00')
                        item.profit = (item.unit_price - item.cost_price) * quantity

                        # Discount logic
                        expected_price = product.selling_price or Decimal('0.00')
                        if item.unit_price < expected_price:
                            item.unit_discount = expected_price - item.unit_price
                            item.total_discount = item.unit_discount * quantity
                        else:
                            item.unit_discount = Decimal('0.00')
                            item.total_discount = Decimal('0.00')

                        total_discount += item.total_discount
                        total_sale_amount += item.subtotal

                        item.save()
                        saved_items.append(item)

                    # Save crate data per category
                    SaleCategoryEmpty.objects.filter(sale=sale).delete()
                    for key in request.POST:
                        if key.startswith('category_empty_brought['):
                            cat_id = key.split('[')[1].split(']')[0]
                            try:
                                cid = int(cat_id)
                            except ValueError:
                                continue

                            expected = Decimal(request.POST.get(f'category_empty_expected[{cid}]', '0'))
                            brought = Decimal(request.POST.get(f'category_empty_brought[{cid}]', '0'))
                            owed = Decimal(request.POST.get(f'category_empty_owed[{cid}]', '0'))

                            SaleCategoryEmpty.objects.create(
                                sale=sale,
                                category_id=cid,
                                empty_expected=expected,
                                empty_brought=brought,
                                empty_owed=owed
                            )

                    # Update sale totals
                    sale.total_amount = total_sale_amount
                    sale.total_discount = total_discount
                    sale.total_amount_paid = Decimal(request.POST.get('total_amount_paid', '0'))
                    sale.save()

                    # --- Confirmed-only side effects ---
                    if sale.status == 'confirmed':
                        paid = sale.total_amount_paid
                        paid = Decimal(str(paid))  # Convert to Decimal once

                        dest = sale.payment_destination
                        if paid > 0:

                            if dest == 'cash':
                                site_setting.cash_balance = (Decimal(site_setting.cash_balance) or Decimal('0.00')) + paid
                                site_setting.save(update_fields=['cash_balance'])
                            elif dest == 'bank':
                                site_setting.balance = (Decimal(site_setting.balance) or Decimal('0.00')) + paid
                                site_setting.save(update_fields=['balance'])
                            elif dest == 'driver' and sale.driver:
                                wallet, _ = StaffWalletModel.objects.get_or_create(staff=sale.driver)
                                wallet.balance = (wallet.balance or Decimal('0.00')) + paid
                                wallet.save(update_fields=['balance'])

                        # Customer wallet debt
                        if sale.customer and sale.total_amount_left > 0:
                            wallet, _ = CustomerWalletModel.objects.get_or_create(customer=sale.customer)
                            wallet.balance += sale.total_amount_left
                            wallet.save(update_fields=['balance'])

                        # Category crates in
                        for ce in SaleCategoryEmpty.objects.filter(sale=sale):
                            ce.category.number_of_empty += float(ce.empty_brought)
                            ce.category.save(update_fields=['number_of_empty'])

                        debt_by_cat = defaultdict(Decimal)
                        for ce in SaleCategoryEmpty.objects.filter(sale=sale):
                            if ce.empty_owed > 0:
                                debt_by_cat[ce.category_id] += ce.empty_owed

                        for cid, debt in debt_by_cat.items():
                            ccd, _ = CustomerCrateDebtModel.objects.get_or_create(
                                customer=sale.customer, category_id=cid
                            )
                            ccd.crate += Decimal(str(debt))
                            ccd.save(update_fields=['crate'])

                        driver = sale.driver or None

                        # Log

                        staff_url = reverse('staff_detail', kwargs={'pk': staff_member.pk}) if staff_member else '#'
                        sale_url = reverse('sale_detail', kwargs={'pk': sale.pk})

                        log_html = f"""
                        <div class='bg-success text-white p-2' style='border-radius:5px;'>
                          <p>
                            <b><a href="{staff_url}" class="text-white text-decoration-underline">{escape(staff_member.full_name.title())}</a></b>
                            confirmed sale <b>#{sale.transaction_id}</b>.<br>
                            <b>Total:</b> ₦{sale.total_amount:.2f} &nbsp;|&nbsp;
                            <b>Paid:</b> ₦{sale.total_amount_paid:.2f} &nbsp;|&nbsp;
                            <b>Owed:</b> ₦{sale.total_amount_left:.2f}<br>
                            <a href="{sale_url}" class="btn btn-sm btn-light mt-2">View Receipt</a>
                            <span class='float-end'>{now():%Y-%m-%d %H:%M:%S}</span>
                          </p>
                        </div>
                        """

                        ActivityLogModel.objects.create(
                            log=log_html,
                            user=request.user,
                            category='sales',
                            keywords='sale__confirmed',
                            customer=sale.customer,
                            driver=driver
                        )
                        messages.success(request, f"Sale #{sale.transaction_id} confirmed.")
                    else:
                        messages.success(request, f"Sale #{sale.transaction_id} recorded as PENDING.")

                    return redirect('sale_detail', pk=sale.pk)
        else:
            messages.error(request, "Please correct the errors below.")

    context = {
        'sale_form': sale_form,
        'formset': formset,
        'title': 'Record New Sale',
        'product_list': ProductModel.objects.all(),
        'customer_list': CustomerModel.objects.all(),
        'staff_list': StaffModel.objects.all(),
        'product_data_for_frontend_json': product_data_for_frontend_json,
        'empty_form': SaleItemCreateFormSet(queryset=SaleItemModel.objects.none()).empty_form,
        'site_setting': site_setting,
        'empty_formset': empty_formset,
    }
    return render(request, 'sale/create.html', context)


class SaleDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = SaleModel
    permission_required = 'sale.view_salemodel'
    template_name = 'sale/detail.html'
    context_object_name = 'sale'

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related(
                'customer',
                'customer__customer_wallet',
                'driver',
                'created_by',
            )
            .prefetch_related(
                Prefetch(
                    'items',
                    queryset=SaleItemModel.objects.select_related('product__category')
                                                    .order_by('id'),
                    to_attr='prefetched_items'
                )
            )
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        sale = self.object

        ctx['title']       = f"Sale Details: #{sale.transaction_id}"
        ctx['sale_items']  = getattr(sale, 'prefetched_items', sale.items.all())
        # Directly query the SaleCategoryEmpty rows for this sale:
        ctx['empty_rows']  = SaleCategoryEmpty.objects.filter(sale=sale)
        ctx['site_info'] = SiteInfoModel.objects.first()
        return ctx


class SaleListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Displays a list of all sales.
    """
    model = SaleModel
    permission_required = 'sale.view_salemodel' # Ensure user has permission to view sales
    template_name = 'sale/index.html' # This will be the new template for the sale list
    context_object_name = 'sales' # The variable name to use in the template to access the list of sales
    paginate_by = 20 # Optional: Add pagination to display 10 sales per page

    def get_queryset(self):
        """
        Optimize queryset to fetch related customer, driver, and creator data
        in a single query, and order by sale date descending.
        """
        queryset = super().get_queryset()
        queryset = queryset.select_related(
            'customer', # Fetch customer details
            'driver',  # Fetch driver details
            'created_by' # Fetch the User who created the sale
        ).order_by('-sale_date', '-created_at') # Order by sale_date (newest first), then created_at
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'All Sales'
        # You might also want to pass filters or search forms here in the future
        return context

import json
import random

from django.utils.html import escape
from django.utils.timezone import now
from django.views import View
from pytz import timezone as pytz_timezone
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from admin_site.models import SiteSettingModel, ActivityLogModel
from human_resource.models import StaffProfileModel
from inventory.models import *
from django.db.models import Q, Count, Sum, F, DecimalField
from datetime import datetime, date
from urllib.parse import urlencode
from django.contrib.auth import logout
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest, Http404
from inventory.models import *
from inventory.forms import *
from collections import OrderedDict
import logging
logger = logging.getLogger(__name__)


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = CategoryModel
    permission_required = 'inventory.add_productmodel'
    form_class = CategoryForm
    success_message = 'Category Added Successfully'
    template_name = 'inventory/category/index.html'

    def get_success_url(self):
        return reverse('inventory_category_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(reverse('inventory_category_index'))

        return super(CategoryCreateView, self).dispatch(*args, **kwargs)

    def form_invalid(self, form):
        """Handle invalid form by redirecting and flashing errors."""
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = CategoryModel
    permission_required = 'inventory.view_productmodel'
    fields = '__all__'
    template_name = 'inventory/category/index.html'
    context_object_name = "inventory_category_list"

    def get_queryset(self):
        return CategoryModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CategoryForm

        return context


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CategoryModel
    permission_required = 'inventory.add_productmodel'
    form_class = CategoryEditForm
    success_message = 'Category Updated Successfully'
    template_name = 'inventory/category/index.html'

    def get_success_url(self):
        return reverse('inventory_category_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(reverse('inventory_category_index'))

        return super(CategoryUpdateView, self).dispatch(*args, **kwargs)

    def form_invalid(self, form):
        """Handle invalid form by redirecting and flashing errors."""
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CategoryModel
    permission_required = 'inventory.add_productmodel'
    success_message = 'Category Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/category/delete.html'
    context_object_name = "category"

    def get_success_url(self):
        return reverse("inventory_category_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddEmptyAdjustmentView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'inventory.add_productmodel'

    def get(self, request):
        messages.error(request, "Method not supported.")
        return redirect('inventory_category_index')

    def post(self, request):
        form = EmptyAdjustmentForm(request.POST)
        if form.is_valid():
            adjustment = form.save(commit=False)
            adjustment.created_by = request.user
            adjustment.save()
            messages.success(
                request,
                f"Successfully {'added' if adjustment.adjustment_type == 'add' else 'removed'} "
                f"{adjustment.amount} crate(s) for '{adjustment.category.name}'."
            )
        else:
            # Add each form error as a separate message
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
        return redirect('inventory_category_index')


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ProductModel
    permission_required = 'inventory.add_productmodel'
    form_class = ProductForm
    success_message = 'Product Added Successfully'
    template_name = 'inventory/product/create.html'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSettingModel.objects.first()
        return context

    def form_valid(self, form):
        product = form.save(commit=False)
        product.updated_by = self.request.user
        product.save()
        return super().form_valid(form)


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ProductModel
    permission_required = 'inventory.view_productmodel'
    fields = '__all__'
    template_name = 'inventory/product/index.html'
    context_object_name = "product_list"

    def get_queryset(self):
        return ProductModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = CategoryModel.objects.all()
        context['form'] = ProductForm
        return context


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = ProductModel
    permission_required = 'inventory.view_productmodel'
    fields = '__all__'
    template_name = 'inventory/product/detail.html'
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['supplier_list'] = SupplierModel.objects.filter(category=self.object.category)

        stock_in_items = StockInModel.objects.filter(
            Q(stockinsummarymodel__isnull=True) | Q(stockinsummarymodel__status='confirmed'),
            product=self.object
        ).prefetch_related(
            'stockinsummarymodel_set'  # Use prefetch_related for the reverse ManyToMany relation
            # (default related_name is modelname_set)
        ).order_by(
            '-stockinsummarymodel__date', '-quantity_left'  # Ordering still works across relationships
        ).distinct()  # Use distinct to prevent potential duplicates if an item is linked to multiple summaries
        context['stock_list'] = stock_in_items

        context['stock_out_form'] = StockOutForm
        price_history_list = PriceHistoryModel.objects.filter(product=self.object).order_by('change_date')
        context['price_history_list'] = price_history_list
        return context


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ProductModel
    permission_required = 'inventory.add_productmodel'
    form_class = ProductEditForm
    success_message = 'Product Updated Successfully'
    template_name = 'inventory/product/edit.html'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        product = form.save(commit=False)
        product.updated_by = self.request.user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ProductModel
    permission_required = 'inventory.add_productmodel'
    success_message = 'Product Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/product/delete.html'
    context_object_name = "product"

    def get_success_url(self):
        return reverse('product_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SupplierModel
    permission_required = 'inventory.add_suppliermodel'
    form_class = SupplierForm
    success_message = 'Supplier Added Successfully'
    template_name = 'inventory/supplier/create.html'

    def get_success_url(self):
        return reverse('supplier_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        supplier = form.save(commit=False)
        supplier.updated_by = self.request.user
        supplier.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = SupplierModel
    permission_required = 'inventory.view_suppliermodel'
    fields = '__all__'
    template_name = 'inventory/supplier/index.html'
    context_object_name = "supplier_list"

    def get_queryset(self):
        return SupplierModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_list'] = CategoryModel.objects.all()
        context['form'] = SupplierForm
        return context


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = SupplierModel
    permission_required = 'inventory.view_suppliermodel'
    fields = '__all__'
    template_name = 'inventory/supplier/detail.html'
    context_object_name = "supplier"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category_list'] = CategoryModel.objects.all().order_by('name')
        return context


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SupplierModel
    permission_required = 'inventory.add_suppliermodel'
    form_class = SupplierEditForm
    success_message = 'Supplier Updated Successfully'
    template_name = 'inventory/supplier/edit.html'

    def form_valid(self, form):
        supplier = form.save(commit=False)
        supplier.updated_by = self.request.user
        supplier.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('supplier_detail', kwargs={'pk': self.object.pk})


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SupplierModel
    permission_required = 'inventory.add_suppliermodel'
    success_message = 'Supplier Deleted Successfully'
    fields = '__all__'
    template_name = 'inventory/supplier/delete.html'
    context_object_name = "supplier"

    def get_success_url(self):
        return reverse('supplier_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# This helper function needs to be defined in your views.py or an accessible utility file.
# It assumes a link from Django's User model to your StaffModel (e.g., via a StaffProfileModel).
# Adjust it to match your actual user-to-staff relationship.
def get_staff_instance(user):
    """
    Retrieves the StaffModel instance associated with the given Django User.
    Adjust this function based on your actual user-to-staff model relationship.
    For example, if User has a OneToOneField to StaffModel, it could be:
    return StaffModel.objects.get(user=user)
    """
    try:
        # Assuming User -> StaffProfileModel (related_name='staff_profile') -> StaffModel (field named 'staff')
        return user.profile.staff
    except (AttributeError, StaffProfileModel.DoesNotExist):
        logger.warning(f"Staff profile not found for user: {user.username}")
        # Consider a more robust way to handle this, e.g., redirect to profile creation
        # For now, it will return None and the calling view will handle the error message.
        return None


@login_required
@permission_required("inventory.add_stockinmodel", raise_exception=True)
def product_pre_stock_in_create_view(request):
    context = {
        'category_list': CategoryModel.objects.all().order_by('name')
    }
    return render(request, 'inventory/stock/select_category.html', context)


# --- Stock In Views ---
@login_required
@permission_required("inventory.add_stockinmodel", raise_exception=True)
def product_stock_in_create_view(request):
    """
    Handles creation of new stock-in summaries.
    The status (pending/confirmed) is determined by the form.
    If 'confirmed', inventory is updated immediately.
    """
    stock_in_summary_form = StockInSummaryForm()
    formset = StockInCreateFormSet(queryset=StockInModel.objects.none())
    site_setting = SiteSettingModel.objects.first()

    if request.method == 'POST':
        stock_in_summary_form = StockInSummaryForm(request.POST)
        formset = StockInCreateFormSet(request.POST, queryset=StockInModel.objects.none())

        if stock_in_summary_form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    staff_member = get_staff_instance(request.user)

                    if staff_member is None:
                        messages.error(request, 'Staff profile not found for the logged-in user. Cannot record stock-in.')
                        return redirect(reverse('login')) # Or appropriate redirect

                    # 1. Save the StockInSummary (Header)
                    stock_in_summary = stock_in_summary_form.save(commit=False)
                    stock_in_summary.created_by = staff_member
                    stock_in_summary.is_tampered = False # Always false on creation

                    total_cost = Decimal('0.00')
                    newly_created_stock_in_items = []

                    for form in formset:
                        if form.has_changed() and not form.cleaned_data.get('DELETE'):
                            item = form.save(commit=False)
                            total_cost += item.quantity_added * item.unit_cost_price

                    if total_cost > stock_in_summary.supplier.balance:
                        messages.error(request,
                                       f'Insufficient cash balance: Needed ₦{total_cost:,.2f}, Available ₦{stock_in_summary.supplier.balance:,.2f}')
                        return redirect('product_stock_in_create')

                    stock_in_summary.save()

                    newly_created_stock_in_items = []

                    # 2. Save the individual StockInModel items from the formset
                    # We save with commit=True here to get IDs for the ManyToMany,
                    # but since we are in an atomic transaction, it will rollback if needed.
                    for form in formset:
                        if form.has_changed() and not form.cleaned_data.get('DELETE'):
                            stock_in_item = form.save(commit=False) # Save temporarily to get the instance
                            stock_in_item.created_by = staff_member
                            stock_in_item.save() # Now saves to DB within the atomic block
                            newly_created_stock_in_items.append(stock_in_item)

                    # 3. Link StockInModel instances to StockInSummaryModel via ManyToMany
                    stock_in_summary.products.set(newly_created_stock_in_items)

                    # === Manual activity log after setting products ===
                    product_count = len(newly_created_stock_in_items)
                    total_cost = sum([item.total_cost_price for item in newly_created_stock_in_items])

                    staff_html = (
                        f"<a href='{reverse('staff_detail', kwargs={'pk': staff_member.pk})}'><b>{escape(staff_member.full_name)}</b></a>"
                        if staff_member else "Unknown Staff"
                    )

                    log_html = f"""
                    <div class='bg-primary text-white p-2' style='border-radius: 5px;'>
                        <p>
                            {staff_html} recorded a <b>{stock_in_summary.status.upper()}</b> stock-in summary.<br>
                            <b>Products:</b> {product_count} &nbsp; | &nbsp;
                            <b>Total Cost:</b> ₦{total_cost:,.2f}
                            <br>
                            <a href='{reverse('product_stock_in_detail', kwargs={'pk': stock_in_summary.pk})}'
                               class='btn btn-sm btn-light mt-2'>
                               View Receipt
                            </a>
                            <span class='float-end'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span>
                        </p>
                    </div>
                    """

                    ActivityLogModel.objects.create(
                        log=log_html,
                        user=request.user,
                        category='inventory',
                        supplier=stock_in_summary.supplier,
                        keywords='inventory__stockin'
                    )

                    # --- LOGIC: Commit to inventory if status is 'confirmed' ---
                    if stock_in_summary.status == 'confirmed':
                        # === Deduct total cost from SiteSetting balance ===

                        supplier = stock_in_summary.supplier
                        sold_category = supplier.category
                        empty = stock_in_summary.empty

                        sold_category.number_of_empty -= empty
                        sold_category.save()

                        if empty > stock_in_summary.total_empty:
                            supplier.balance += (empty - stock_in_summary.total_empty) * site_setting.price_for_empty
                        else:
                            supplier.balance -= (stock_in_summary.total_empty - empty) * site_setting.price_for_empty

                        supplier.balance = Decimal(str(supplier.balance)) - total_cost
                        supplier.save()

                        # === Variables for log messages ===
                        supplier_name = escape(supplier.name)
                        category_name = supplier.category.name.upper() if supplier.category else 'N/A'
                        shortfall_or_surplus = empty - stock_in_summary.total_empty
                        price_per_empty = site_setting.price_for_empty
                        total_empty_adjustment = abs(shortfall_or_surplus) * price_per_empty
                        final_balance = f"₦{supplier.balance:,.2f}"

                        # Line 1: Main cost
                        line_1 = f"1: ₦{total_cost:,.2f} was removed from supplier <b>{supplier_name}</b>'s wallet due to purchase."

                        # Line 2: Empty removal log
                        line_2 = f"2: {empty} empty container{'s' if empty != 1 else ''} was removed for category <b>{category_name}</b>."

                        # Line 3: Adjustment due to shortfall/surplus
                        if shortfall_or_surplus < 0:
                            line_3 = f"3: A further ₦{total_empty_adjustment:,.2f} was removed due to shortfall of {-shortfall_or_surplus} empty container{'s' if shortfall_or_surplus != -1 else ''}."
                        elif shortfall_or_surplus > 0:
                            line_3 = f"3: ₦{total_empty_adjustment:,.2f} was added to supplier account due to surplus of {shortfall_or_surplus} empty container{'s' if shortfall_or_surplus != 1 else ''}."
                        else:
                            line_3 = "3: No additional charge or refund for empty containers."

                        # Line 4: Final balance
                        line_4 = f"4: Current supplier balance is: <b>{final_balance}</b>."

                        # Combine all lines into a log
                        full_log_html = f"""
                        <div class='bg-dark text-white p-2' style='border-radius: 5px;'>
                            <p>{line_1}<br>
                            {line_2}<br>
                            {line_3}<br>
                            {line_4}
                            <span class='float-end'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
                        </div>
                        """

                        # Create the log
                        ActivityLogModel.objects.create(
                            log=full_log_html,
                            user=request.user,
                            supplier=supplier,
                            category='finance',
                            keywords='finance__supplier_deduction'
                        )

                        # Proceed with product inventory update and selling price update
                        for item in newly_created_stock_in_items:
                            product = item.product
                            if product.quantity is None:
                                product.quantity = Decimal('0.00')
                            product.quantity += item.quantity_added
                            product.save(update_fields=['quantity'])

                            # --- Conditioned Logic: Update ProductModel's selling_price only if confirmed ---
                            new_selling_price = item.unit_selling_price
                            if new_selling_price is not None:
                                if hasattr(product, 'selling_price') and product.selling_price != new_selling_price:
                                    product.selling_price = new_selling_price
                                    product.updated_by = request.user
                                    product.save(update_fields=['selling_price', 'updated_by'])

                            new_cost_price = item.unit_cost_price

                            if new_cost_price is not None:
                                if hasattr(product, 'last_cost_price') and product.last_cost_price != new_cost_price:
                                    product.last_cost_price = new_cost_price
                                    product.save()
                        messages.success(request, f'Stock-in receipt #{stock_in_summary.pk} confirmed and inventory updated successfully!')
                    else: # Status is 'pending'
                        messages.success(request, f'Stock-in receipt #{stock_in_summary.pk} recorded as PENDING. It will not affect inventory until manually confirmed.')
                    # --- END LOGIC ---
                return redirect(reverse('product_stock_in_detail', kwargs={'pk': stock_in_summary.id}))

            except ValueError as ve: # Catch the specific ValueError from our validation
                messages.error(request, f'Stock-in Failed: {ve}')
                logger.exception(f"Stock-in transaction failed due to category capacity: {ve}")
            except Exception as e:
                messages.error(request, f'Error processing stock-in: {e}')
                logger.exception("Stock-in transaction failed during creation due to unexpected error")
        else:
            messages.error(request, 'Please correct the errors below.')

    # Prepare product_category_map for frontend initialization
    product_category_map = {
        str(p.id): str(p.category.id)
        for p in ProductModel.objects.select_related('category').all()
        if p.category # Ensure product has a category
    }

    try:
        selected_category_id = int(request.GET.get('category', 0))
        selected_category = CategoryModel.objects.get(id=selected_category_id)
    except ValueError:
        selected_category = None

    context = {
        'stock_in_summary_form': stock_in_summary_form,
        'selected_category': selected_category,
        'payment_source_list': SupplierModel.objects.filter(category=selected_category),
        'formset': formset,
        'title': 'Receive New Stock',
        'category_list': CategoryModel.objects.all().values('id', 'name', 'number_of_empty'),
        'site_setting': site_setting,
        'minimum_unit_profit': SiteSettingModel.objects.first().minimum_unit_profit if SiteSettingModel.objects.exists() else Decimal('0.00'),
        'product_category_map': product_category_map, # Pass the map for frontend
    }
    return render(request, 'inventory/stock/stock_in.html', context)


def api_product_search(request):
    """
    API endpoint for searching products.
    Filters products by 'q' (query string) and 'category_id' (optional).
    Returns product ID, name, category name, category ID, last known cost price,
    selling price, and **current quantity in stock**.
    """
    query = request.GET.get('q', '')
    category_id = request.GET.get('category_id')

    products = ProductModel.objects.all()

    if query:
        products = products.filter(Q(name__icontains=query))

    if category_id:
        products = products.filter(category_id=category_id)

    results = []
    for product in products[:20]:
        selling_price = product.selling_price or Decimal('0.00')
        current_quantity = product.quantity or Decimal('0.00') # Get product's current quantity

        results.append({
            'id': product.id,
            'type': product.type,
            'name': product.name,
            'category_id': product.category.id if hasattr(product, 'category') and product.category else None,
            'category_name': product.category.name if hasattr(product, 'category') and product.category else 'N/A',
            'selling_price': float(selling_price),      # Convert Decimal to float for JSON
            'quantity': float(current_quantity),        # NEW: Include current quantity in stock
            'last_cost_price': float(product.last_cost_price)
        })

    return JsonResponse(results, safe=False)


class StockInListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Lists all StockInSummaryModel records, regardless of status.
    """
    model = StockInSummaryModel
    permission_required = 'inventory.view_stockinmodel'
    template_name = 'inventory/stock/index.html'
    context_object_name = "inventory_stock_list"

    def get_queryset(self):
        return StockInSummaryModel.objects.filter(status='confirmed').annotate(
            num_products=Count('products')
        ).order_by('-date', '-created_at')


def calculate_category_quantities(stock_in_items):
    """Aggregates total quantity_added per category from a list of StockInModel instances."""
    category_quantities = {}
    for item in stock_in_items:
        # Ensure product and category are not None and can be resolved
        if item.product and item.product.category:
            category_id = item.product.category.id
            quantity_to_add = item.quantity_added
            if category_id not in category_quantities:
                category_quantities[category_id] = Decimal('0.00')
            category_quantities[category_id] += quantity_to_add
    return category_quantities


class StockInSummaryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = StockInSummaryModel
    form_class = StockInSummaryForm
    template_name = 'inventory/stock/stock_in_update.html'
    permission_required = 'inventory.change_stockinmodel'
    success_message = 'Stock-in summary updated successfully!'

    def get_queryset(self):
        # Prevent editing tampered records
        return super().get_queryset().filter(is_tampered=False)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.is_tampered:
            messages.error(request, f'Stock receipt #{obj.pk} has been tampered with and cannot be edited.')
            return redirect('product_stock_in_detail', pk=obj.pk)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stock_in_summary = self.object
        context['stock_in_summary_form'] = context['form']
        context['title'] = f'Edit Stock-In #{stock_in_summary.pk}'

        formset_queryset = stock_in_summary.products.select_related('product').all()
        if self.request.POST:
            context['formset'] = StockInFormSet(self.request.POST, queryset=formset_queryset)
        else:
            context['formset'] = StockInFormSet(queryset=formset_queryset)
            context['empty_form'] = StockInFormSet(queryset=StockInModel.objects.none()).empty_form

        # Add categories, site settings, and product-category mapping as needed here
        # (Same as your existing get_context_data, omitted for brevity)

        return context

    def form_valid(self, form):
        stock_in_summary = self.get_object()
        staff_member = get_staff_instance(self.request.user)
        if not staff_member:
            messages.error(self.request, 'Staff profile not found for the logged-in user. Cannot update stock.')
            return self.form_invalid(form)

        formset = StockInFormSet(self.request.POST, queryset=stock_in_summary.products.all())
        if not formset.is_valid():
            messages.error(self.request, 'Please correct errors in the product items.')
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

        try:
            with transaction.atomic():
                # Save original state for diff calculation
                original_items = list(stock_in_summary.products.select_related('product', 'product__category').all())
                original_status = stock_in_summary.status
                original_supplier = stock_in_summary.supplier
                original_total_cost = stock_in_summary.total_cost or Decimal('0.00')

                # Save the updated stock-in summary
                updated_summary = form.save(commit=False)
                if hasattr(updated_summary, 'updated_by'):
                    updated_summary.updated_by = staff_member
                updated_summary.save()

                # Process the stock-in items formset
                updated_items = []
                for f in formset:
                    if f.cleaned_data.get('DELETE', False):
                        if f.instance.pk:
                            f.instance.delete()
                    else:
                        item = f.save(commit=False)
                        if not item.pk:
                            item.created_by = staff_member
                        item.save()
                        updated_items.append(item)
                updated_summary.products.set(updated_items)

                # Helper function to calculate quantities per category from list of items
                def calc_cat_qty(items):
                    cat_qty = {}
                    for item in items:
                        cat_id = item.product.category.id if item.product and item.product.category else None
                        if cat_id is not None:
                            cat_qty[cat_id] = cat_qty.get(cat_id, Decimal('0.00')) + Decimal(item.quantity_added)
                    return cat_qty

                original_cat_qty = calc_cat_qty(original_items)
                updated_cat_qty = calc_cat_qty(updated_items)

                # Calculate difference per category to update number_of_empty
                cat_qty_diff = {}
                for cat_id in set(original_cat_qty.keys()).union(updated_cat_qty.keys()):
                    old_qty = original_cat_qty.get(cat_id, Decimal('0.00'))
                    new_qty = updated_cat_qty.get(cat_id, Decimal('0.00'))
                    cat_qty_diff[cat_id] = new_qty - old_qty

                # Fetch relevant categories
                categories = CategoryModel.objects.filter(id__in=cat_qty_diff.keys())
                category_map = {c.id: c for c in categories}

                # Check if confirming stock-in (pending->confirmed)
                is_confirming = (original_status == 'pending' and updated_summary.status == 'confirmed')
                # Or unconfirming (confirmed->pending)
                is_unconfirming = (original_status == 'confirmed' and updated_summary.status == 'pending')
                # Or updating while confirmed
                is_reconfirming = (original_status == 'confirmed' and updated_summary.status == 'confirmed')
                # Pending updated to pending (just update)
                is_pending_update = (original_status == 'pending' and updated_summary.status == 'pending')

                # Rollback inventory if status was confirmed previously
                if original_status == 'confirmed':
                    for item in original_items:
                        product = item.product
                        product.quantity = (product.quantity or Decimal('0.00')) - Decimal(item.quantity_added)
                        product.save(update_fields=['quantity'])

                        cat = category_map.get(product.category.id) if product.category else None
                        if cat:
                            cat.number_of_empty = (cat.number_of_empty or Decimal('0.00')) + Decimal(item.quantity_added)
                            cat.save(update_fields=['number_of_empty'])

                    # Rollback supplier wallet for original cost
                    if original_supplier:
                        original_supplier.wallet_balance = (original_supplier.wallet_balance or Decimal('0.00')) + original_total_cost
                        original_supplier.save(update_fields=['wallet_balance'])

                # Confirm or update confirmed status: apply new inventory and wallet changes
                if updated_summary.status == 'confirmed':
                    # Check category capacities for the new quantities
                    for cat_id, diff_qty in cat_qty_diff.items():
                        if diff_qty > 0:
                            cat = category_map.get(cat_id)
                            if not cat:
                                raise ValueError(f"Category id {cat_id} not found.")
                            if diff_qty > (cat.number_of_empty or Decimal('0.00')):
                                raise ValueError(
                                    f"Category '{cat.name}' capacity insufficient for added quantity {diff_qty}."
                                )

                    # Apply category capacity adjustments
                    for cat_id, diff_qty in cat_qty_diff.items():
                        cat = category_map.get(cat_id)
                        if cat:
                            cat.number_of_empty = (cat.number_of_empty or Decimal('0.00')) - diff_qty
                            cat.save(update_fields=['number_of_empty'])

                    # Apply updated product quantities and selling prices
                    for item in updated_items:
                        product = item.product
                        product.quantity = (product.quantity or Decimal('0.00')) + Decimal(item.quantity_added)
                        if item.unit_selling_price is not None:
                            product.selling_price = item.unit_selling_price
                        product.save(update_fields=['quantity', 'selling_price'])

                    # Update supplier wallet: deduct new total cost
                    new_total_cost = updated_summary.total_cost or Decimal('0.00')
                    supplier = updated_summary.supplier
                    if supplier:
                        supplier.wallet_balance = (supplier.wallet_balance or Decimal('0.00')) - new_total_cost
                        supplier.save(update_fields=['wallet_balance'])

                # Update status field and save again if changed
                if stock_in_summary.status != updated_summary.status:
                    updated_summary.status = updated_summary.status
                    updated_summary.save(update_fields=['status'])

                # Log the activity (describe main changes)
                ActivityLogModel.objects.create(
                    user=self.request.user,
                    action=(
                        f"Updated Stock-In #{updated_summary.pk} | Status: {original_status} → {updated_summary.status} | "
                        f"Supplier: {original_supplier} → {updated_summary.supplier} | "
                        f"Cost: {original_total_cost} → {updated_summary.total_cost}"
                    ),
                    model_name='StockInSummaryModel',
                    object_id=updated_summary.pk
                )

                messages.success(self.request, self.success_message)
                return redirect(self.get_success_url())

        except ValueError as ve:
            messages.error(self.request, f"Update failed: {ve}")
            logger.exception(f"StockInSummary update validation error: {ve}")
            return self.render_to_response(self.get_context_data(form=form, formset=formset))
        except Exception as e:
            messages.error(self.request, f"An unexpected error occurred: {e}")
            logger.exception("StockInSummary update error", exc_info=True)
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_success_url(self):
        return reverse('product_stock_in_detail', kwargs={'pk': self.object.pk})



class StockInSummaryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = StockInSummaryModel
    template_name = 'inventory/stock/delete.html'
    permission_required = "inventory.change_stockinmodel"
    success_url = reverse_lazy('stock_in_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.is_tampered:
            messages.error(self.request, "This stock-in record has been tampered with and cannot be deleted.")
            raise Http404
        return obj

    def form_valid(self, form):
        stock_in_summary = self.get_object()
        original_status = stock_in_summary.status
        related_stock_in_items = list(stock_in_summary.products.all())
        supplier = stock_in_summary.supplier
        empty = stock_in_summary.empty or 0
        total_quantity = stock_in_summary.total_quantity or 0

        try:
            with transaction.atomic():
                if original_status == 'confirmed':
                    # Load settings
                    site_settings = SiteSettingModel.objects.first()
                    if not site_settings:
                        raise ValueError("Site settings not configured.")
                    price_for_empty = Decimal(str(site_settings.price_for_empty))

                    # Reverse all inventory changes
                    for item in related_stock_in_items:
                        product = item.product
                        qty_added = Decimal(str(item.quantity_added or 0))
                        product.quantity = (product.quantity or Decimal('0')) - qty_added
                        product.save(update_fields=['quantity'])

                        if product.category:
                            category = CategoryModel.objects.get(id=product.category.id)
                            category.number_of_empty = (Decimal(str(category.number_of_empty or 0))) + qty_added
                            category.save(update_fields=['number_of_empty'])

                    # Reverse supplier balance
                    supplier_balance = Decimal(str(supplier.balance or 0))
                    total_cost = sum([Decimal(str(item.total_cost_price)) for item in related_stock_in_items])
                    shortfall_or_surplus = empty - total_quantity
                    empty_adjustment = Decimal(abs(shortfall_or_surplus)) * price_for_empty

                    if shortfall_or_surplus < 0:
                        supplier_balance += empty_adjustment
                    elif shortfall_or_surplus > 0:
                        supplier_balance -= empty_adjustment

                    supplier_balance += total_cost
                    supplier.balance = supplier_balance
                    supplier.save(update_fields=['balance'])

                    # Activity Log (Inventory)
                    staff_user = self.request.user
                    log_html = f"""
                    <div class='bg-danger text-white p-2' style='border-radius: 5px;'>
                        <p>
                            <b>{escape(staff_user.get_full_name())}</b> <b>deleted</b> confirmed stock receipt #{stock_in_summary.pk}.<br>
                            Inventory quantities and category capacities were rolled back.
                            <span class='float-end'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span>
                        </p>
                    </div>
                    """
                    ActivityLogModel.objects.create(
                        log=log_html,
                        user=staff_user,
                        category='inventory',
                        supplier=supplier,
                        keywords='inventory__stockin_delete'
                    )

                    # Activity Log (Finance)
                    log2 = f"""
                    <div class='bg-dark text-white p-2' style='border-radius: 5px;'>
                        <p>
                            1: ₦{total_cost:,.2f} was refunded to <b>{escape(supplier.name)}</b> due to deletion.<br>
                            2: {empty} empty container{'s' if empty != 1 else ''} was returned to category <b>{supplier.category.name}</b>.<br>
                            {"3: ₦" + f"{empty_adjustment:,.2f} was refunded" if shortfall_or_surplus < 0 else "3: ₦" + f"{empty_adjustment:,.2f} was removed" if shortfall_or_surplus > 0 else "3: No additional adjustment made."}<br>
                            4: Supplier final balance: <b>₦{supplier.balance:,.2f}</b>.
                            <span class='float-end'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span>
                        </p>
                    </div>
                    """
                    ActivityLogModel.objects.create(
                        log=log2,
                        user=staff_user,
                        category='finance',
                        supplier=supplier,
                        keywords='finance__supplier_delete_refund'
                    )

                    messages.success(self.request, f"Confirmed stock-in #{stock_in_summary.pk} deleted and all related changes reversed.")
                else:
                    messages.info(self.request, f"Pending stock-in #{stock_in_summary.pk} deleted. No inventory changes were necessary.")

                # Proceed with deletion
                self.object.delete()
                return redirect(self.get_success_url())

        except Exception as e:
            messages.error(self.request, f"Error deleting stock-in #{stock_in_summary.pk}: {e}")
            logger.exception(f"Error during stock-in deletion for PK {stock_in_summary.pk}")
            return redirect(self.get_success_url())


class PendingStockInListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Lists only StockInSummaryModel records with 'pending' status,
    ready for confirmation. Requires a specific permission.
    """
    model = StockInSummaryModel
    permission_required = 'inventory.view_stockinmodel'  # Custom permission for processing
    template_name = 'inventory/stock/pending_stock_in.html'
    context_object_name = "pending_stock_in_summaries"

    def get_queryset(self):
        return StockInSummaryModel.objects.filter(
            status='pending'
        ).annotate(
            num_products=Count('products')
        ).filter(
            num_products__gt=0
        ).order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Pending Stock Receipts for Confirmation'
        return context


@login_required
@permission_required("inventory.view_stockinmodel", raise_exception=True)
def product_stock_in_detail_view(request, pk):
    """
    Displays the details of a specific stock-in summary and its associated products.
    Includes status, total cost, and conditional actions (confirm, edit, delete).
    """
    stock_in_summary = get_object_or_404(StockInSummaryModel, pk=pk)
    stock_in_items = stock_in_summary.products.all().select_related('product')  # Eager load product

    # Calculate total receipt cost
    total_receipt_cost_agg = stock_in_items.aggregate(
        total_cost=Sum(F('quantity_added') * F('unit_cost_price'), output_field=DecimalField())
    )['total_cost'] or Decimal('0.00')

    # Example: Calculate total quantity added (you might already have this in your model)
    total_quantity_added_agg = stock_in_items.aggregate(
        total_qty=Sum('quantity_added')
    )['total_qty'] or Decimal('0.00')

    # Assume you have empty_qty stored somewhere (example: from category or stock_in_summary)
    # Replace this with your actual source of empty_qty
    empty_qty = Decimal('100.00')  # placeholder, replace with actual logic to get empty_qty

    # Calculate adjusted empty quantity safely
    adjusted_empty_qty = empty_qty - total_quantity_added_agg

    context = {
        'stock_in_summary': stock_in_summary,
        'stock_in_items': stock_in_items,
        'total_receipt_cost': total_receipt_cost_agg,
        'total_quantity_added': total_quantity_added_agg,
        'empty_qty': empty_qty,
        'adjusted_empty_qty': adjusted_empty_qty,
        'title': f'Stock Receipt #{stock_in_summary.id} Details',
    }
    return render(request, 'inventory/stock/detail.html', context)


@login_required
@permission_required("inventory.change_stockinmodel", raise_exception=True)
def process_pending_stock_in_view(request, pk):
    """
    Confirm a pending StockInSummaryModel, commit quantities to inventory,
    update selling prices, deduct payment from supplier,
    and handle empty container adjustments as per creation logic.
    """

    stock_in_summary = get_object_or_404(StockInSummaryModel, pk=pk)

    # Prevent double processing or tampered receipts
    if stock_in_summary.status == 'confirmed':
        messages.info(request, 'This stock receipt has already been confirmed.')
        return redirect(reverse('product_stock_in_detail', kwargs={'pk': pk}))

    if stock_in_summary.is_tampered:
        messages.error(request, 'This receipt has been tampered with and cannot be confirmed.')
        return redirect(reverse('product_stock_in_detail', kwargs={'pk': pk}))

    if request.method == 'POST':
        try:
            with transaction.atomic():
                stock_in_items = stock_in_summary.products.all().select_related('product', 'product__category')
                site_setting = SiteSettingModel.objects.first()
                if not site_setting:
                    raise ValueError("Site settings not configured.")

                # STEP 1: Calculate total cost of stock-in items (all products)
                total_cost = sum([Decimal(str(item.total_cost_price or '0')) for item in stock_in_items])

                # STEP 2: Supplier & Empty container logic
                supplier = stock_in_summary.supplier
                if not supplier:
                    raise ValueError("Supplier information missing for this stock receipt.")

                sold_category = supplier.category
                if sold_category is None:
                    raise ValueError("Supplier category missing.")

                # Get the values from the stock_in_summary model
                empty_brought_by_supplier = Decimal(str(stock_in_summary.empty or '0')) # User-entered 'Empty Brought'
                bottles_stocked_in_transaction = Decimal(str(stock_in_summary.total_empty or '0')) # Calculated 'Total Empty (Bottles Stocked)'

                # Validate if empties brought exceed category's *current* empty capacity (if applicable)
                # This logic assumes sold_category.number_of_empty is the current count of empty containers for that category.
                # If 'empty_brought_by_supplier' is meant to reduce this, then ensure it doesn't go negative.
                current_category_empties = Decimal(str(sold_category.number_of_empty or '0'))
                if empty_brought_by_supplier > current_category_empties:
                     # This is a warning/error depending on your business rule.
                     # If you allow negative empty counts temporarily, this can be a warning.
                     # If not, it should raise an error.
                     # For now, keeping your original error message structure.
                     raise ValueError(
                         f"Stock-in empty containers ({empty_brought_by_supplier}) exceed current category empty containers ({current_category_empties})."
                     )

                # Deduct the empty containers brought by the supplier from the category's count
                sold_category.number_of_empty = current_category_empties - empty_brought_by_supplier
                sold_category.save(update_fields=['number_of_empty'])

                price_for_empty = Decimal(str(site_setting.price_for_empty or '0'))
                supplier_balance = Decimal(str(supplier.balance)) if supplier.balance is not None else Decimal('0')

                # CRITICAL CORRECTION: Calculate shortfall/surplus based on empties brought vs. bottles stocked
                shortfall_or_surplus_for_balance = empty_brought_by_supplier - bottles_stocked_in_transaction

                if shortfall_or_surplus_for_balance > 0: # Supplier brought more empties than bottles stocked (surplus for supplier)
                    supplier_balance += shortfall_or_surplus_for_balance * price_for_empty
                elif shortfall_or_surplus_for_balance < 0: # Supplier brought fewer empties than bottles stocked (shortfall for supplier)
                    supplier_balance -= abs(shortfall_or_surplus_for_balance) * price_for_empty
                # If shortfall_or_surplus_for_balance is 0, no change needed for balance from empties

                # Validate if supplier has enough balance *after* empty adjustment for the total cost
                if total_cost > supplier_balance:
                    raise ValueError(
                        f"Insufficient supplier balance after empty container adjustment. Needed ₦{total_cost:,.2f}, Available ₦{supplier_balance:,.2f}"
                    )

                # Deduct the total cost of all products
                supplier_balance -= total_cost
                supplier.balance = supplier_balance
                supplier.save(update_fields=['balance'])

                # STEP 4: Update product quantities and prices
                for item in stock_in_items:
                    product = item.product

                    if product.quantity is None:
                        product.quantity = Decimal('0')

                    qty_added = Decimal(str(item.quantity_added)) if item.quantity_added is not None else Decimal('0')
                    product.quantity += qty_added

                    # Update selling price if different
                    new_selling_price = item.unit_selling_price
                    new_cost_price = item.unit_cost_price

                    fields_to_update = ['quantity']

                    if new_selling_price is not None and hasattr(product, 'selling_price'):
                        if product.selling_price != new_selling_price:
                            product.selling_price = new_selling_price
                            fields_to_update.append('selling_price')

                    if new_cost_price is not None and hasattr(product, 'last_cost_price'):
                        if product.last_cost_price != new_cost_price:
                            product.last_cost_price = new_cost_price
                            fields_to_update.append('last_cost_price')

                    product.save(update_fields=fields_to_update)

                # STEP 5: Mark stock_in_summary as confirmed
                stock_in_summary.status = 'confirmed'
                stock_in_summary.save(update_fields=['status'])

                # STEP 6: Activity log
                staff_member = get_staff_instance(request.user)
                product_count = stock_in_items.count()

                staff_html = (
                    f"<a href='{reverse('staff_detail', kwargs={'pk': staff_member.pk})}'>"
                    f"<b>{escape(staff_member.full_name)}</b></a>" if staff_member else "Unknown Staff"
                )

                # Log 1: Confirmation of stock-in
                log_html = f"""
                <div class='bg-primary text-white p-2' style='border-radius: 5px;'>
                    <p>
                        {staff_html} <b>confirmed</b> stock receipt #{stock_in_summary.pk}.<br>
                        <b>Products:</b> {product_count} &nbsp; | &nbsp;
                        <b>Total Cost:</b> ₦{total_cost:,.2f}
                        <br>
                        <a href='{reverse('product_stock_in_detail', kwargs={'pk': stock_in_summary.pk})}'
                           class='btn btn-sm btn-light mt-2'>View Receipt</a>
                        <span class='float-end'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span>
                    </p>
                </div>
                """

                ActivityLogModel.objects.create(
                    log=log_html,
                    user=request.user,
                    category='inventory',
                    supplier=supplier,
                    keywords='inventory__stockin_confirm'
                )

                # Log 2: Supplier deduction + empty container adjustment log (like create_view)
                # Use the corrected variables for logging
                shortfall_or_surplus_for_log = empty_brought_by_supplier - bottles_stocked_in_transaction
                total_empty_adjustment_for_log = abs(shortfall_or_surplus_for_log) * price_for_empty
                final_balance = f"₦{supplier.balance:,.2f}"
                supplier_name = escape(supplier.name)
                category_name = supplier.category.name.upper() if supplier.category else 'N/A'

                line_1 = f"1: ₦{total_cost:,.2f} was removed from supplier <b>{supplier_name}</b>'s wallet due to purchase."
                line_2 = f"2: {empty_brought_by_supplier} empty container{'s' if empty_brought_by_supplier != 1 else ''} was removed for category <b>{category_name}</b>."
                if shortfall_or_surplus_for_log < 0:
                    line_3 = f"3: A further ₦{total_empty_adjustment_for_log:,.2f} was removed due to shortfall of {-shortfall_or_surplus_for_log} bottle empty container{'s' if shortfall_or_surplus_for_log != -1 else ''}."
                elif shortfall_or_surplus_for_log > 0:
                    line_3 = f"3: ₦{total_empty_adjustment_for_log:,.2f} was added to supplier account due to surplus of {shortfall_or_surplus_for_log} bottle empty container{'s' if shortfall_or_surplus_for_log != 1 else ''}."
                else:
                    line_3 = "3: No additional charge or refund for bottle empty containers."

                line_4 = f"4: Current supplier balance is: <b>{final_balance}</b>."

                full_log_html = f"""
                <div class='bg-dark text-white p-2' style='border-radius: 5px;'>
                    <p>{line_1}<br>
                    {line_2}<br>
                    {line_3}<br>
                    {line_4}
                    <span class='float-end'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
                </div>
                """

                ActivityLogModel.objects.create(
                    log=full_log_html,
                    user=request.user,
                    supplier=supplier,
                    category='finance',
                    keywords='finance__supplier_deduction_confirm'
                )

                messages.success(request, f'Stock receipt #{pk} confirmed and inventory updated successfully!')
                return redirect(reverse('product_stock_in_detail', kwargs={'pk': pk}))

        except ValueError as ve:
            messages.error(request, f'Confirmation Failed: {ve}')
            logger.exception(f"Stock-in confirmation validation failed: {ve}")
        except Exception as e:
            messages.error(request, f'Unexpected error during confirmation: {e}')
            logger.exception(f"Error confirming stock-in summary {pk}")

    # Render confirmation page on GET or error
    context = {
        'stock_in_summary': stock_in_summary,
        'stock_in_items': stock_in_summary.products.all().select_related('product'),
        'title': f'Confirm Stock Receipt #{stock_in_summary.pk}',
    }
    return render(request, 'inventory/stock/process_pending_stock_in.html', context)



class StockOutCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = StockOutModel
    permission_required = 'inventory.add_stockinmodel'
    form_class = StockOutForm
    success_url = reverse_lazy('stock_out_list')
    template_name = 'inventory/stock/stock_out_form.html'

    def form_valid(self, form):
        try:
            staff_member = get_staff_instance(self.request.user)
            if staff_member is None:
                messages.error(self.request, "Staff profile not found for the logged-in user. Cannot record stock out.")
                return self.form_invalid(form)

            form.instance.created_by = staff_member

            stock_in_item = form.instance.stock
            quantity_removed = form.instance.quantity_removed

            parent_summaries = stock_in_item.stockinsummarymodel_set.all()

            if not parent_summaries.exists():
                if stock_in_item.product.initial_quantity_left == 0:
                    form.add_error(None,
                                   "No valid stock receipt found for the selected stock item. Cannot process stock out.")
                    return self.form_invalid(form)

            for parent_summary in parent_summaries:
                if parent_summary.status != 'confirmed':
                    form.add_error(None,
                                   f"Cannot stock out from receipt #{parent_summary.pk}. It is still PENDING. Please confirm it first.")
                    return self.form_invalid(form)

            if quantity_removed <= Decimal('0.00'):
                form.add_error('quantity_removed', "Quantity to remove must be greater than zero.")
                return self.form_invalid(form)

            if stock_in_item.quantity_left < quantity_removed:
                form.add_error('quantity_removed',
                               f"Cannot remove {quantity_removed}. Only {stock_in_item.quantity_left} available in this specific stock batch.")
                return self.form_invalid(form)

            if not form.instance.reason or not form.instance.reason.strip():
                form.add_error('reason', "Reason for removal is required.")
                return self.form_invalid(form)

            with transaction.atomic():
                form.save()  # This triggers StockOutModel's save() method

                # --- NEW LOGIC START ---
                # Update quantity_stocked_out on the StockInModel
                stock_in_item.quantity_stocked_out = (stock_in_item.quantity_stocked_out or Decimal(
                    '0.00')) + quantity_removed

                # Update status of StockInModel if quantity_left becomes zero or less
                if stock_in_item.quantity_left <= Decimal('0.00'):
                    stock_in_item.status = 'finished'  # Assuming 'finished' is a valid status for StockInModel

                stock_in_item.save(
                    update_fields=['quantity_stocked_out', 'quantity_left', 'status'])  # Save the updated fields
                # --- NEW LOGIC END ---

                product = stock_in_item.product
                if product.quantity is None:
                    product.quantity = Decimal('0.00')
                product.quantity -= quantity_removed
                product.save(update_fields=['quantity'])

                if form.cleaned_data.get('stock_out_empty') and product.category:
                    category = product.category
                    current_num_empty = Decimal(
                        str(category.number_of_empty)) if category.number_of_empty is not None else Decimal('0.00')

                    category.number_of_empty = current_num_empty - quantity_removed
                    category.save(update_fields=['number_of_empty'])
                    messages.info(self.request,
                                  f"Category '{category.name}' capacity reduced by {quantity_removed} due to stock out.")

            messages.success(self.request,
                             f'Stock out of {quantity_removed} Crate of {product.name} successfully recorded.')

            return redirect(self.get_success_url())

        except Exception as e:
            logger.exception("Stock out create view failed unexpectedly.")
            messages.error(self.request, f'An unexpected error occurred during stock-out: {e}')
            return self.form_invalid(form)

    def form_invalid(self, form):
        for field, field_errors in form.errors.items():
            for error in field_errors:
                if field == '__all__':
                    messages.error(self.request, f"Error: {error}")
                else:
                    messages.error(self.request, f"Error in '{form.fields[field].label}': {error}")

        messages.error(self.request, 'Please correct the errors in the form below to complete the stock out.')

        product_pk = None
        if form.instance.stock and form.instance.stock.product:
            product_pk = form.instance.stock.product.pk

        if product_pk:
            return redirect(reverse('product_detail', kwargs={'pk': product_pk}))
        else:
            messages.error(self.request, "Could not determine the product to redirect to. Please try again.")
            return redirect(reverse_lazy('stock_out_list'))

    def get_success_url(self):
        if self.object and self.object.stock and self.object.stock.product:
            return reverse('product_detail', kwargs={'pk': self.object.stock.product.pk})
        return reverse_lazy('stock_out_list')


class StockOutIndexView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = StockOutModel
    permission_required = 'inventory.view_stockinmodel'
    template_name = 'inventory/stock/stock_out_list.html'
    context_object_name = "stock_out_list"
    paginate_by = 10

    def get_queryset(self):
        return StockOutModel.objects.select_related('stock__product').order_by('-created_at')


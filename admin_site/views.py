from datetime import datetime
from decimal import Decimal

from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Sum, F, DecimalField, ExpressionWrapper
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import logout
from admin_site.models import *
from admin_site.forms import *
from django.utils.timezone import now, localtime
from django.http import JsonResponse, HttpResponse
from finance.models import ExpenseModel, StaffSalarySummaryModel, CashTransferModel
from human_resource.models import StaffProfileModel, StaffWalletModel
from inventory.models import ProductModel, CategoryModel, StockInModel, StockInSummaryModel
from sale.models import CustomerCrateDebtModel, SaleModel, SaleItemModel, CustomerWalletModel, \
    CustomerDebtRepaymentModel
from django.db.models import Sum, F, OuterRef, Subquery, DecimalField, IntegerField, Value
from django.db.models import Sum, F, OuterRef, Subquery, DecimalField, IntegerField, Value
from django.db.models.functions import Coalesce



def correct(request):
    sale_list = SaleItemModel.objects.all()
    for sale in sale_list:
        product = sale.product
        stock = StockInModel.objects.filter(product=product).first()
        stock.quantity_sold += sale.quantity
        stock.quantity_left -= sale.quantity
        
        stock.save()
        
    return HttpResponse('done')
    

class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_site/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_count'] = ProductModel.objects.count()

        # Existing total stock quantity (for all products) - if you still need it
        context['total_stock_quantity'] = (
                ProductModel.objects.aggregate(total=Sum('quantity'))['total'] or Decimal('0.00')
        )

        # NEW: Calculate total quantity specifically for 'bottle' type products
        total_bottle_stock_quantity = (
                ProductModel.objects.filter(type='bottle')
                .aggregate(total=Sum('quantity'))['total'] or Decimal('0.00')
        )
        context['total_bottle_stock_quantity'] = total_bottle_stock_quantity

        context['customer_count'] = CustomerModel.objects.count()

        context['low_stock_count'] = ProductModel.objects.filter(
            quantity__lte=F('reorder_level')
        ).count()

        context['total_empty_crates'] = (
                CategoryModel.objects.aggregate(total=Sum('number_of_empty'))['total'] or Decimal('0.00')
        )

        context['crates_owed_by_customers'] = (
                CustomerCrateDebtModel.objects.aggregate(total=Sum('crate'))['total'] or Decimal('0.00')
        )

        settings = SiteSettingModel.objects.first()
        context[
            'petty_cash_balance'] = settings.petty_cash_balance if settings and settings.petty_cash_balance is not None else Decimal(
            '0.00')

        context['today'] = localtime(now()).strftime('%A, %d %B %Y')
        stock_worth_data = StockInModel.objects.aggregate(
            # Total worth at cost price
            total_worth_at_cost=Coalesce(
                Sum(F('quantity_left') * F('unit_cost_price')),
                Decimal('0.00'),
                output_field=DecimalField()
            ),
            # Total worth at selling price
            total_worth_at_selling=Coalesce(
                Sum(F('quantity_left') * F('unit_selling_price')),
                Decimal('0.00'),
                output_field=DecimalField()
            )
        )

        context['total_worth_at_cost'] = stock_worth_data['total_worth_at_cost']
        context['total_worth_at_selling'] = stock_worth_data['total_worth_at_selling']

        site_setting = SiteSettingModel.objects.first()
        # Ensure site_setting and price_for_empty are not None before use
        price_for_empty_decimal = Decimal(
            str(site_setting.price_for_empty)) if site_setting and site_setting.price_for_empty is not None else Decimal(
            '0.00')

        # UPDATED: 'unliquidated_empties' now uses total_bottle_stock_quantity
        context['unliquidated_empties'] = price_for_empty_decimal * total_bottle_stock_quantity

        total_empty_crates_decimal = Decimal(str(context['total_empty_crates']))

        # Now, perform all calculations using Decimal objects for precision
        context['worth_of_empty_crates'] = total_empty_crates_decimal * price_for_empty_decimal

        # Ensure total_worth_at_selling is a Decimal for robust calculation
        total_worth_at_selling_decimal = Decimal(str(context['total_worth_at_selling']))

        context['total_worth'] = total_worth_at_selling_decimal + context['worth_of_empty_crates'] + context['unliquidated_empties']

        return context


      
def sign_in_view(request):
    """
    Handles user sign-in requests, authenticating users and redirecting
    them based on their roles (superuser or staff).
    """
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        # Determine the intended route after successful login
        intended_route = request.POST.get('next') or request.GET.get('next')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is None:
            # If authentication fails, display an error message and redirect to login
            messages.error(request, 'Invalid username or password.')
            return redirect(reverse('login')) # Ensure 'login' is the URL name for your sign-in page

        # --- Authentication Successful: Proceed with Login and Role-based Redirection ---

        # Log the user in
        login(request, user)

        # Set session expiry based on 'remember_me' preference
        if remember_me:
            request.session.set_expiry(3600 * 24 * 30)  # 30 days
        else:
            request.session.set_expiry(0)  # Session expires when browser closes

        # Handle Superuser login
        if user.is_superuser:
            messages.success(request, f'Welcome back, {user.username.title()}! You have full administrative access.')
            return redirect(intended_route or reverse('admin_dashboard'))

        # Handle Staff user login
        try:
            # Attempt to retrieve the staff profile for the authenticated user
            # Assuming StaffProfileModel has a ForeignKey/OneToOneField to Django's User model
            staff_profile = StaffProfileModel.objects.get(user=user)

            # Check if the staff profile is active/authorized (e.g., 'staff' field is True)
            if staff_profile.staff:
                messages.success(request, f'Welcome back, {staff_profile.user.username.title()}!.')
                return redirect(intended_route or reverse('admin_dashboard'))
            else:
                # If staff profile exists but is not active
                messages.error(request, 'Your staff account is currently inactive. Please contact support.')
                logout(request) # Log out the user immediately if their staff access is invalid
                return redirect(reverse('login'))

        except StaffProfileModel.DoesNotExist:
            # If the user is not a superuser and does not have a staff profile
            messages.error(request, 'Access denied. Your account does not have the necessary privileges.')
            logout(request) # Log out the user immediately if they don't have required roles
            return redirect(reverse('login'))

    # Render the sign-in form for GET requests
    return render(request, 'admin_site/login.html')


def sign_out_view(request):
    logout(request)
    return redirect(reverse('login'))


@login_required
def user_change_password_view(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']

        # Verify the current password
        if not request.user.check_password(current_password):
            messages.error(request, 'Incorrect current password.')
            return redirect(reverse('change_password'))

        # Check if the new passwords match
        if len(new_password1) < 8:
            messages.error(request, 'Password must have at least 8 characters.')
            return redirect(reverse('change_password'))

        if not re.match("^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]+$", new_password1):
            messages.error(request, 'Password must contain both letters and numbers.')
            return redirect(reverse('change_password'))

        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            return redirect(reverse('change_password'))

        # Update the user's password
        user = request.user
        user.set_password(new_password1)
        user.save()

        # Update the user's session with the new password
        update_session_auth_hash(request, user)

        logout(request)

        messages.success(request, 'Password successfully changed. Please log in with the new password.')
        return redirect('login')

    return render(request, 'admin_site/change_password.html')


class ActivityLogView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'admin_site.add_dashboardmodel'
    model = ActivityLogModel
    template_name = 'admin_site/activity_log.html'
    context_object_name = 'activity_log_list'
    paginate_by = 15

    def get_queryset(self):
        qs = ActivityLogModel.objects.all().order_by('-id')

        # --- Filters ---
        category = self.request.GET.get('category', 'all')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        keyword = self.request.GET.get('search')

        # Default dates to today
        today_str = now().date().isoformat()
        start_date = start_date or today_str
        end_date = end_date or today_str

        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            qs = qs.filter(created_at__date__range=(start, end))
        except ValueError:
            pass

        if category != 'all':
            qs = qs.filter(category__iexact=category)

        if keyword:
            qs = qs.filter(log__icontains=keyword)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ['all', 'inventory', 'finance', 'sales']
        context['selected_category'] = self.request.GET.get('category', 'all')
        context['start_date'] = self.request.GET.get('start_date', now().date().isoformat())
        context['end_date'] = self.request.GET.get('end_date', now().date().isoformat())
        context['search'] = self.request.GET.get('search', '')
        return context


def admin_sign_out_view(request):
    logout(request)
    return redirect(reverse('admin_login'))


class SiteInfoDetailView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'admin_site/site_info/detail.html'
    permission_required = 'admin_site.change_siteinfomodel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_info = SiteInfoModel.objects.first()

        if not site_info:
            form = SiteInfoForm()
            is_site_info = False
        else:
            form = SiteInfoForm(instance=site_info)
            is_site_info = True
        context['form'] = form
        context['is_site_info'] = is_site_info
        context['site_info'] = site_info
        context['site_setting'] = SiteSettingModel.objects.first()
        return context


class SiteInfoCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SiteInfoModel
    permission_required = 'admin_site.change_siteinfomodel'
    form_class = SiteInfoForm
    template_name = 'admin_site/site_info/create.html'
    success_message = 'Info updated Successfully'

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SiteInfoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SiteInfoModel
    permission_required = 'admin_site.change_siteinfomodel'
    form_class = SiteInfoForm
    template_name = 'admin_site/site_info/create.html'
    success_message = 'Info updated Successfully'

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SiteSettingDetailView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'admin_site/site_setting/detail.html'
    permission_required = 'admin_site.change_sitesettingmodel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_setting = SiteSettingModel.objects.first()

        if not site_setting:
            form = SiteSettingForm()
            is_site_setting = False
        else:
            form = SiteSettingForm(instance=site_setting)
            is_site_setting = True
        context['form'] = form
        context['is_site_setting'] = is_site_setting
        context['site_setting'] = site_setting
        return context


class SiteSettingCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = SiteSettingModel
    permission_required = 'admin_site.change_sitesettingmodel'
    form_class = SiteSettingForm
    template_name = 'admin_site/site_setting/create.html'
    success_message = 'Setting updated Successfully'

    def get_success_url(self):
        return reverse('site_setting_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class SiteSettingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SiteSettingModel
    permission_required = 'admin_site.change_sitesettingmodel'
    form_class = SiteSettingEditForm
    template_name = 'admin_site/site_setting/create.html'
    success_message = 'Setting updated Successfully'

    def get_success_url(self):
        return reverse('site_setting_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        # Set the current user temporarily on the instance
        form.instance._changed_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_setting'] = SiteSettingModel.objects.first()
        return context


def parse_date_safe(date_str, fallback):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return fallback



@login_required
def performing_customers_view(request):
    today = now().date()
    first_day = today.replace(day=1)

    raw_start = request.GET.get('start_date')
    raw_end = request.GET.get('end_date')
    order_by = request.GET.get('order_by', 'total_profit')

    start_date_dt = parse_date_safe(raw_start, first_day)
    end_date_dt = parse_date_safe(raw_end, today)

    # ✅ Validation logic
    if start_date_dt > end_date_dt:
        messages.warning(request, "Start date cannot be after end date.")
        start_date_dt = first_day
        end_date_dt = today
    elif start_date_dt > today or end_date_dt > today:
        messages.warning(request, "Dates cannot be in the future.")
        start_date_dt = first_day
        end_date_dt = today

    # Fetch and annotate
    correct_sales_total_amount_subquery_customer = SaleModel.objects.filter(
        customer=OuterRef('customer__id'),
        status='confirmed',
        sale_date__date__range=[start_date_dt, end_date_dt]
    ).values('customer').annotate(
        sum_total_amount_per_customer=Sum('total_amount', output_field=DecimalField())
    ).values('sum_total_amount_per_customer')

    sales = SaleModel.objects.filter(
        status='confirmed',
        sale_date__date__range=[start_date_dt, end_date_dt],
        customer__isnull=False
    ).values('customer__id', 'customer__full_name').annotate(
        total_amount=Coalesce(Subquery(correct_sales_total_amount_subquery_customer), Value(0.00),
                              output_field=DecimalField()),
        total_quantity=Coalesce(Sum('items__quantity'), Value(0), output_field=IntegerField()),
        total_profit=Coalesce(Sum('items__profit'), Value(0.00), output_field=DecimalField())
    ).order_by(f'-{order_by}')

    paginator = Paginator(sales, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'sales': page_obj,
        'start_date': start_date_dt.strftime('%Y-%m-%d'),
        'end_date': end_date_dt.strftime('%Y-%m-%d'),
        'order_by': order_by
    }

    return render(request, 'admin_site/statistic/performing_customers.html', context)


@login_required
@permission_required("admin_site.view_dashboardmodel", raise_exception=True)
def performing_drivers_view(request):
    today = now().date()
    first_day = today.replace(day=1)

    raw_start = request.GET.get('start_date')
    raw_end = request.GET.get('end_date')
    order_by = request.GET.get('order_by', 'total_profit')

    start_date_dt = parse_date_safe(raw_start, first_day)
    end_date_dt = parse_date_safe(raw_end, today)

    # ✅ Validation
    if start_date_dt > end_date_dt:
        messages.warning(request, "Start date cannot be after end date.")
        start_date_dt = first_day
        end_date_dt = today
    elif start_date_dt > today or end_date_dt > today:
        messages.warning(request, "Dates cannot be in the future.")
        start_date_dt = first_day
        end_date_dt = today

    correct_sales_total_amount_subquery = SaleModel.objects.filter(
        driver=OuterRef('driver__id'),
        status='confirmed',
        sale_date__date__range=[start_date_dt, end_date_dt]
    ).values('driver').annotate(
        sum_total_amount_per_driver=Sum('total_amount', output_field=DecimalField())
    ).values('sum_total_amount_per_driver')

    sales = SaleModel.objects.filter(
        status='confirmed',
        driver__isnull=False,
        sale_date__date__range=[start_date_dt, end_date_dt]
    ).values('driver__id', 'driver__full_name').annotate(
        total_amount=Coalesce(Subquery(correct_sales_total_amount_subquery), Value(0.00), output_field=DecimalField()),
        total_quantity=Coalesce(Sum('items__quantity'), Value(0), output_field=IntegerField()),
        total_profit=Coalesce(Sum('items__profit'), Value(0.00), output_field=DecimalField()),
    ).order_by(f'-{order_by}')

    paginator = Paginator(sales, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'sales': page_obj,
        'start_date': start_date_dt.strftime('%Y-%m-%d'),
        'end_date': end_date_dt.strftime('%Y-%m-%d'),
        'order_by': order_by
    }

    return render(request, 'admin_site/statistic/performing_drivers.html', context)


@login_required
@permission_required("admin_site.view_dashboardmodel", raise_exception=True)
def performing_products_view(request):
    today = now().date()
    first_day = today.replace(day=1)

    raw_start = request.GET.get('start_date')
    raw_end = request.GET.get('end_date')
    order_by = request.GET.get('order_by', 'total_quantity')

    start_date_dt = parse_date_safe(raw_start, first_day)
    end_date_dt = parse_date_safe(raw_end, today)

    # ✅ Validate date range
    if start_date_dt > end_date_dt:
        messages.warning(request, "Start date cannot be after end date.")
        start_date_dt = first_day
        end_date_dt = today
    elif start_date_dt > today or end_date_dt > today:
        messages.warning(request, "Dates cannot be in the future.")
        start_date_dt = first_day
        end_date_dt = today

    # Aggregate product performance
    product_sales = SaleItemModel.objects.filter(
        sale__status='confirmed',
        sale__sale_date__date__range=(start_date_dt, end_date_dt)
    ).values(
        'product__id',
        'product__name',
        'product__category__name'
    ).annotate(
        total_quantity=Sum('quantity'),
        total_amount=Sum(F('unit_price') * F('quantity')),  # This calculates sum per SaleItem correctly
        total_profit=Sum('profit')
    ).order_by(f'-{order_by}')

    paginator = Paginator(product_sales, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'sales': page_obj,
        'start_date': start_date_dt.strftime('%Y-%m-%d'),
        'end_date': end_date_dt.strftime('%Y-%m-%d'),
        'order_by': order_by
    }

    return render(request, 'admin_site/statistic/performing_products.html', context)
    

@login_required
@permission_required("admin_site.view_dashboardmodel", raise_exception=True)
def product_sale_view(request):
    today = now().date()
    first_day = today.replace(day=1)

    raw_start = request.GET.get('start_date')
    raw_end = request.GET.get('end_date')

    start_date = parse_date_safe(raw_start, first_day)
    end_date = parse_date_safe(raw_end, today)

    if start_date > end_date or start_date > today or end_date > today:
        messages.error(request, "Invalid date range.")
        start_date = first_day
        end_date = today

    sale_items = SaleItemModel.objects.filter(
        sale__status='confirmed',
        sale__sale_date__date__range=[start_date, end_date]
    ).select_related('product', 'sale__customer').annotate(
        selling_price=F('unit_price'),
        cost=F('cost_price'),
        profit_each=F('profit'),
        total_selling_price=F('unit_price') * F('quantity'),
    ).order_by('-sale__sale_date')

    paginator = Paginator(sale_items, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items': page_obj,
        'start_date': start_date.strftime('%Y-%m-%d'),
        'end_date': end_date.strftime('%Y-%m-%d'),
    }

    return render(request, 'admin_site/statistic/product_sales.html', context)


@login_required
@permission_required("admin_site.view_dashboardmodel", raise_exception=True)
def statistic_dashboard_view(request):
    today = now().date()
    first_day = today.replace(day=1)

    # parse & validate dates from GET, fallback to month‐to‐date
    def parse_date_safe(s, fallback):
        try:
            return datetime.strptime(s, "%Y-%m-%d").date()
        except:
            return fallback

    start_str = request.GET.get('start_date', '')
    end_str   = request.GET.get('end_date',   '')
    start_date = parse_date_safe(start_str, first_day)
    end_date   = parse_date_safe(end_str,   today)

    # Prevent future dates and ensure start <= end
    if start_date > today or end_date > today or start_date > end_date:
        start_date, end_date = first_day, today

    sales_qs = SaleModel.objects.filter(
        status='confirmed',
        sale_date__date__range=(start_date, end_date)
    )

    # 1. Total Sales (₦)
    total_sales = sales_qs.aggregate(total=Sum('total_amount'))['total'] or Decimal('0.00')

    # 2. Total Products Sold (sum of quantities)
    total_products_sold = sales_qs.aggregate(qty=Sum('items__quantity'))['qty'] or 0

    # 3. Total Outstanding Customer Debt
    total_debt_owed = CustomerWalletModel.objects.aggregate(sum=Sum('balance'))['sum'] or Decimal('0.00')

    # 4. Total Debt Paid (sum of repayments in date range)
    total_debt_paid = CustomerDebtRepaymentModel.objects.filter(
        created_at__date__range=(start_date, end_date)
    ).aggregate(sum=Sum('amount_paid'))['sum'] or Decimal('0.00')

    # 5. Total Expense
    total_expense = ExpenseModel.objects.filter(
        date__range=(start_date, end_date)
    ).aggregate(sum=Sum('amount'))['sum'] or Decimal('0.00')

    # 6. Total Salary Paid
    total_salary_paid = StaffSalarySummaryModel.objects.filter(
        month__range=(start_date, end_date)
    ).aggregate(sum=Sum('total_payment'))['sum'] or Decimal('0.00')

    # 7. Total Stock‑in Amount (sum of quantity_added × unit_cost_price)
    total_stock_in_amount = StockInModel.objects.filter(
        date_added__range=(start_date, end_date)
    ).aggregate(
        sum=Sum(
            ExpressionWrapper(
                F('quantity_added') * F('unit_cost_price'),
                output_field=DecimalField()
            )
        )
    )['sum'] or Decimal('0.00')

    # 8. COGS (sum of sold qty × cost_price from each sale item)
    cogs = sales_qs.aggregate(
        sum=Sum(
            ExpressionWrapper(
                F('items__quantity') * F('items__cost_price'),
                output_field=DecimalField()
            )
        )
    )['sum'] or Decimal('0.00')

    # 9. Gross Profit = sales – cogs
    gross_profit = total_sales - cogs

    # 10. Net Profit after expenses & salaries
    net_profit = gross_profit - total_expense - total_salary_paid

    context = {
        'start_date': start_date,
        'end_date':   end_date,
        'total_sales':            total_sales,
        'total_products_sold':    total_products_sold,
        'total_debt_owed':        total_debt_owed,
        'total_debt_paid':        total_debt_paid,
        'total_expense':          total_expense,
        'total_salary_paid':      total_salary_paid,
        'total_stock_in_amount':  total_stock_in_amount,
        'gross_profit':           gross_profit,
        'net_profit':             net_profit,
    }
    return render(request, 'admin_site/statistic/dashboard.html', context)


class OverviewDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'admin_site/overview_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # ==================== PRODUCT DATA ====================
        context['product_count'] = ProductModel.objects.count()

        # Get all categories with their empties
        categories = CategoryModel.objects.all()
        category_empties = []
        total_empties_count = Decimal('0.00')
        total_empties_worth = Decimal('0.00')

        for category in categories:
            empty_count = Decimal(str(category.number_of_empty))
            price_per_empty = Decimal(str(category.price_for_empty))
            worth = empty_count * price_per_empty

            category_empties.append({
                'name': category.name,
                'count': empty_count,
                'price': price_per_empty,
                'worth': worth
            })

            total_empties_count += empty_count
            total_empties_worth += worth

        context['category_empties'] = category_empties
        context['total_empties_count'] = total_empties_count
        context['total_empties_worth'] = total_empties_worth

        # ==================== TOTAL CASH ====================
        settings = SiteSettingModel.objects.first()

        context['bank_balance'] = Decimal(str(settings.balance)) if settings else Decimal('0.00')
        context['cash_balance'] = Decimal(str(settings.cash_balance)) if settings else Decimal('0.00')
        context['petty_cash_balance'] = Decimal(str(settings.petty_cash_balance)) if settings else Decimal('0.00')

        # Vendor (Supplier) balance
        vendor_balance = SupplierModel.objects.aggregate(total=Sum('balance'))['total'] or 0.0
        context['vendor_balance'] = Decimal(str(vendor_balance))

        # Staff wallet total (all staff)
        staff_wallets = StaffWalletModel.objects.all()
        staff_wallet_total = sum(Decimal(str(w.balance)) for w in staff_wallets)
        context['staff_wallet_total'] = staff_wallet_total

        # Calculate total cash
        context['total_cash'] = (
                context['bank_balance'] +
                context['cash_balance'] +
                context['petty_cash_balance'] +
                context['vendor_balance'] +
                context['staff_wallet_total']
        )

        # ==================== INVENTORY ====================
        # Total stock quantity
        context['total_stock_quantity'] = (
                ProductModel.objects.aggregate(total=Sum('quantity'))['total'] or 0
        )

        # Cost of drink (total worth at cost)
        # Replace the StockInModel aggregation with this:
        product_worth_data = ProductModel.objects.aggregate(
            total_worth_at_cost=Sum(F('quantity') * F('last_cost_price')),
            total_worth_at_selling=Sum(F('quantity') * F('selling_price')),
        )

        context['cost_of_drink'] = Decimal(str(product_worth_data['total_worth_at_cost'] or 0))
        context['sale_value_of_drink'] = Decimal(str(product_worth_data['total_worth_at_selling'] or 0))

        # Cost of empty per category (already calculated above)
        context['cost_of_empties'] = total_empties_worth

        # ==================== TOTAL ASSET ====================
        # Account Receivable (customer debt)
        customer_debt = CustomerWalletModel.objects.aggregate(
            total=Sum('balance')
        )['total'] or 0.0
        context['account_receivable'] = Decimal(str(customer_debt))

        # Total Asset calculation
        context['total_asset'] = (
                context['account_receivable'] +
                context['total_cash'] +
                context['cost_of_empties'] +
                context['sale_value_of_drink']
        )

        context['today'] = localtime(now()).strftime('%A, %d %B %Y')

        return context
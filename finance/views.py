import json
import logging
import random
from django.forms import modelformset_factory
from django.utils.html import escape
from django.utils.timezone import localtime, now
from django.views import View
from pytz import timezone as pytz_timezone
from datetime import datetime, time
from django.db.models import Q, Sum, F, DecimalField, Value
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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
from finance.forms import ExpenseTypeForm, StaffBonusForm, StaffDeductionForm, ExpenseForm, StaffSalaryForm, \
    StaffSalaryPaymentFormSet, StaffSalaryPaymentForm, CashTransferForm
from finance.models import ExpenseTypeModel, StaffBonusModel, StaffDeductionModel, ExpenseModel, StaffSalaryModel, \
    StaffSalaryPaymentModel, CashTransferModel, StaffSalarySummaryModel
from human_resource.models import StaffModel, StaffWalletModel
from inventory.models import *
from django.db.models import Q, Count, Sum
from datetime import datetime, date, timedelta
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from sale.models import SaleModel, SaleItemModel, CustomerWalletModel, CustomerCrateDebtModel, \
    CustomerDebtRepaymentModel, CustomerCrateReturnModel
import pytz

# Define your local timezone
LOCAL_TZ = pytz.timezone('Africa/Lagos')
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


class ExpenseTypeCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ExpenseTypeModel
    permission_required = 'finance.add_expensemodel'
    form_class = ExpenseTypeForm
    success_message = 'Expense Type Added Successfully'
    template_name = 'finance/expense_type/index.html'

    def get_success_url(self):
        return reverse('expense_type_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class ExpenseTypeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ExpenseTypeModel
    permission_required = 'finance.add_expensemodel'
    template_name = 'finance/expense_type/index.html'
    context_object_name = "expense_type_list"

    def get_queryset(self):
        return ExpenseTypeModel.objects.all().order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ExpenseTypeForm()
        return context


class ExpenseTypeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ExpenseTypeModel
    permission_required = 'finance.add_expensemodel'
    form_class = ExpenseTypeForm
    success_message = 'Expense Type Updated Successfully'
    template_name = 'finance/expense_type/index.html'

    def get_success_url(self):
        return reverse('expense_type_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class ExpenseTypeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ExpenseTypeModel
    permission_required = 'finance.add_expensemodel'
    success_message = 'Expense Type Deleted Successfully'
    template_name = 'finance/expense_type/delete.html'
    context_object_name = "expense_type"

    def get_success_url(self):
        return reverse('expense_type_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# -------------------------
# Expense Views
# -------------------------

class ExpenseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ExpenseModel
    # Note: Django's default permission scheme is app_label.view_modelname
    permission_required = 'finance.view_expensemodel'
    template_name = 'finance/expense/index.html'
    context_object_name = "expense_list"

    def get_queryset(self):
        return ExpenseModel.objects.select_related('type', 'created_by').order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ExpenseForm()
        context['site_setting'] = SiteSettingModel.objects.first()
        return context


class ExpenseCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ExpenseModel
    permission_required = 'finance.add_expensemodel'
    form_class = ExpenseForm
    success_message = 'Expense Added Successfully'

    def get_success_url(self):
        return reverse('expense_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        error_message = "Please correct the errors below: "
        for field, errors in form.errors.items():
            label = form.fields[field].label or field.replace('_', ' ').title()
            error_message += f" {label}: {', '.join(errors)}"
        messages.error(self.request, error_message)
        return redirect(self.get_success_url())

    def form_valid(self, form):
        site_setting = SiteSettingModel.objects.first()
        expense_amount = form.cleaned_data['amount']
        payment_source = form.cleaned_data['payment_source']

        # Determine which balance to check and update
        if payment_source == 'PETTY_CASH':
            if site_setting.petty_cash_balance < float(expense_amount):
                messages.error(self.request,
                               f"Insufficient petty cash. Available: ₦{site_setting.petty_cash_balance:,.2f}")
                return redirect(self.get_success_url())
            site_setting.petty_cash_balance -= float(expense_amount)
            update_field = 'petty_cash_balance'
        else:  # ACCOUNT_BALANCE
            if site_setting.balance < float(expense_amount):
                messages.error(self.request, f"Insufficient account balance. Available: ₦{site_setting.balance:,.2f}")
                return redirect(self.get_success_url())
            site_setting.balance -= float(expense_amount)
            update_field = 'balance'

        site_setting.save(update_fields=[update_field])

        # Save the expense
        form.instance.created_by = self.request.user
        response = super().form_valid(form)

        # Log activity
        staff = get_staff_instance(self.request.user)
        expense = form.instance
        local_time = localtime(now(), pytz.timezone('Africa/Lagos')).strftime("%Y-%m-%d %H:%M:%S")
        staff_url = reverse('staff_detail', kwargs={'pk': staff.pk}) if staff else "#"
        source_display = expense.get_payment_source_display()  # "Petty Cash" or "Account Balance"

        log_html = f"""
        <div class='bg-danger text-white p-2' style='border-radius:5px;'>
            <p>
                <b><a href="{staff_url}" class="text-white text-decoration-underline">
                    {escape(staff.full_name.title()) if staff else 'System'}
                </a></b> recorded an expense of 
                <b>₦{expense.amount:,.2f}</b> from <b>{source_display}</b> under <b>{escape(expense.type.name)}</b>.<br>
                Remark: {escape(expense.remark or "N/A")}
                <span class='float-end'>{local_time}</span>
            </p>
        </div>
        """
        ActivityLogModel.objects.create(log=log_html, user=self.request.user, category='finance',
                                        keywords='finance__expense_created')
        return response


class ExpenseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ExpenseModel
    permission_required = 'finance.change_expensemodel'
    form_class = ExpenseForm
    success_message = 'Expense Updated Successfully'

    def get_success_url(self):
        return reverse('expense_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        error_message = "Update failed. Please correct the errors: "
        for field, errors in form.errors.items():
            label = form.fields[field].label or field.replace('_', ' ').title()
            error_message += f" {label}: {', '.join(errors)}"
        messages.error(self.request, error_message)
        return redirect(self.get_success_url())

    def form_valid(self, form):
        site_setting = SiteSettingModel.objects.first()
        old_expense = self.get_object()  # Expense instance before update

        # Restrict update if older than 3 hours
        if now() - old_expense.created_at > timedelta(hours=3):
            messages.error(self.request, "You can only edit an expense within 3 hours of creation.")
            return redirect(self.get_success_url())

        # 1. Revert the old transaction by adding the old amount back to its original source
        if old_expense.payment_source == 'PETTY_CASH':
            site_setting.petty_cash_balance += float(old_expense.amount)
        else:  # ACCOUNT_BALANCE
            site_setting.balance += float(old_expense.amount)

        # 2. Validate and apply the new transaction
        new_amount = form.cleaned_data['amount']
        new_source = form.cleaned_data['payment_source']

        if new_source == 'PETTY_CASH':
            if site_setting.petty_cash_balance < float(new_amount):
                messages.error(self.request,
                               f"Update failed. Insufficient petty cash for the new amount. Available: ₦{site_setting.petty_cash_balance:,.2f}")
                return redirect(self.get_success_url())
            site_setting.petty_cash_balance -= float(new_amount)
        else:  # ACCOUNT_BALANCE
            if site_setting.balance < float(new_amount):
                messages.error(self.request,
                               f"Update failed. Insufficient account balance for the new amount. Available: ₦{site_setting.balance:,.2f}")
                return redirect(self.get_success_url())
            site_setting.balance -= float(new_amount)

        site_setting.save()  # Save all changes to balances
        response = super().form_valid(form)

        # Log activity
        staff = get_staff_instance(self.request.user)
        local_time = localtime(now(), pytz.timezone('Africa/Lagos')).strftime("%Y-%m-%d %H:%M:%S")
        staff_url = reverse('staff_detail', kwargs={'pk': staff.pk}) if staff else "#"
        old_source_display = old_expense.get_payment_source_display()
        new_source_display = form.instance.get_payment_source_display()

        log_html = f"""
        <div class='bg-warning text-dark p-2' style='border-radius:5px;'>
            <p>
                <b><a href="{staff_url}" class="text-dark text-decoration-underline">
                    {escape(staff.full_name.title()) if staff else 'System'}
                </a></b> updated an expense. <br>
                Initial: <b>₦{old_expense.amount:,.2f}</b> from <b>{old_source_display}</b>.<br>
                Updated: <b>₦{new_amount:,.2f}</b> from <b>{new_source_display}</b>.
                <span class='float-end'>{local_time}</span>
            </p>
        </div>
        """
        ActivityLogModel.objects.create(log=log_html, user=self.request.user, category='finance',
                                        keywords='finance__expense_updated')

        return response


class ExpenseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ExpenseModel
    permission_required = 'finance.delete_expensemodel'
    success_message = 'Expense deleted successfully.'

    def get_success_url(self):
        return reverse('expense_index')

    # Using form_valid is safer with DeleteView for logic before deletion
    def form_valid(self, form):
        expense = self.get_object()
        site_setting = SiteSettingModel.objects.first()

        # 3-hour restriction
        if (now() - expense.created_at) > timedelta(hours=3):
            messages.error(self.request, "This expense was recorded more than 3 hours ago and cannot be deleted.")
            return redirect(self.get_success_url())

        # Refund the amount to its original source
        if expense.payment_source == 'PETTY_CASH':
            site_setting.petty_cash_balance += float(expense.amount)
            source_display = "Petty Cash"
            update_field = 'petty_cash_balance'
        else:  # ACCOUNT_BALANCE
            site_setting.balance += float(expense.amount)
            source_display = "Account Balance"
            update_field = 'balance'

        site_setting.save(update_fields=[update_field])

        # Log activity
        staff = get_staff_instance(self.request.user)
        staff_url = reverse('staff_detail', kwargs={'pk': staff.pk}) if staff else '#'
        timestamp = localtime(now(), pytz.timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')

        log_html = f"""
        <div class='bg-danger text-white p-2' style='border-radius:5px;'>
            <p>
                <b><a href="{staff_url}" class="text-white text-decoration-underline">{escape(staff.full_name) if staff else 'System'}</a></b>
                deleted an expense of <b>₦{expense.amount:,.2f}</b> (Type: {escape(expense.type.name)}).<br>
                The amount was refunded to <b>{source_display}</b>.<br>
                <span class='float-end'>{timestamp}</span>
            </p>
        </div>
        """
        ActivityLogModel.objects.create(log=log_html, user=self.request.user, category='finance',
                                        keywords='finance__expense_deleted')

        # Call the parent form_valid to perform the deletion
        response = super().form_valid(form)
        return response

class StaffBonusCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = StaffBonusModel
    permission_required = 'finance.add_staffbonusmodel'
    form_class = StaffBonusForm
    success_message = 'Bonus Added Successfully'
    template_name = 'finance/staff_bonus/index.html'

    def get_success_url(self):
        return reverse('staff_bonus_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class StaffBonusListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = StaffBonusModel
    permission_required = 'finance.add_staffbonusmodel'
    template_name = 'finance/staff_bonus/index.html'
    context_object_name = "staff_bonus_list"

    def get_queryset(self):
        return StaffBonusModel.objects.select_related('staff').order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StaffBonusForm()
        return context


class StaffBonusUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StaffBonusModel
    permission_required = 'finance.add_staffbonusmodel'
    form_class = StaffBonusForm
    success_message = 'Bonus Updated Successfully'
    template_name = 'finance/staff_bonus/index.html'

    def get_success_url(self):
        return reverse('staff_bonus_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class StaffBonusDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = StaffBonusModel
    permission_required = 'finance.add_staffbonusmodel'
    success_message = 'Bonus Deleted Successfully'
    template_name = 'finance/staff_bonus/delete.html'
    context_object_name = "bonus"

    def get_success_url(self):
        return reverse('staff_bonus_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StaffDeductionCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = StaffDeductionModel
    permission_required = 'finance.add_staffbonusmodel'
    form_class = StaffDeductionForm
    success_message = 'Deduction Added Successfully'
    template_name = 'finance/staff_deduction/index.html'

    def get_success_url(self):
        return reverse('staff_deduction_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class StaffDeductionListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = StaffDeductionModel
    permission_required = 'finance.add_staffbonusmodel'
    template_name = 'finance/staff_deduction/index.html'
    context_object_name = "staff_deduction_list"

    def get_queryset(self):
        return StaffDeductionModel.objects.select_related('staff').order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StaffDeductionForm()
        return context


class StaffDeductionUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StaffDeductionModel
    permission_required = 'finance.add_staffbonusmodel'
    form_class = StaffDeductionForm
    success_message = 'Deduction Updated Successfully'
    template_name = 'finance/staff_deduction/index.html'

    def get_success_url(self):
        return reverse('staff_deduction_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())


class StaffDeductionDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = StaffDeductionModel
    permission_required = 'finance.add_staffbonusmodel'
    success_message = 'Deduction Deleted Successfully'
    template_name = 'finance/staff_deduction/delete.html'
    context_object_name = "deduction"

    def get_success_url(self):
        return reverse('staff_deduction_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def staff_salary_profile_view(request):
    staff_salaries = StaffSalaryModel.objects.select_related('staff')
    return render(request, 'finance/salary_profile/index.html', {
        'staff_salaries': staff_salaries
    })


@login_required
@permission_required("finance.add_staffsalarypaymentmodel", raise_exception=True)
def staff_salary_profile_update(request):
    # Create or update salary profiles for all staff
    StaffSalaryFormSet = modelformset_factory(
        StaffSalaryModel,
        form=StaffSalaryForm,
        extra=0,
        can_delete=False
    )

    # Ensure all staff have a salary profile
    for staff in StaffModel.objects.all():
        StaffSalaryModel.objects.get_or_create(staff=staff)

    queryset = StaffSalaryModel.objects.all()

    if request.method == 'POST':
        formset = StaffSalaryFormSet(request.POST, queryset=queryset)
        if formset.is_valid():
            with transaction.atomic():
                formset.save()
            return redirect('staff_salary_profile_index')
        return HttpResponse(formset.errors)
    else:
        formset = StaffSalaryFormSet(queryset=queryset)

    return render(request, 'finance/salary_profile/update.html', {
        'formset': formset
    })


def get_first_day_of_current_month():
    today = date.today()
    return today.replace(day=1)


@transaction.atomic
@login_required
@permission_required("finance.add_staffsalarypaymentmodel", raise_exception=True)
def salary_payment_create(request):
    current_month = get_first_day_of_current_month()

    if StaffSalaryPaymentModel.objects.filter(month=current_month).exists():
        messages.warning(request, f"Salary already paid for {current_month.strftime('%B %Y')}.")
        return redirect('salary_payment_view', month=current_month.strftime('%Y-%m-%d'))

    staff_salaries = StaffSalaryModel.objects.select_related('staff').all()
    site_setting = SiteSettingModel.objects.first()

    StaffSalaryPaymentFormSet = modelformset_factory(
        StaffSalaryPaymentModel,
        form=StaffSalaryPaymentForm,
        extra=len(staff_salaries),
        can_delete=False,
    )

    if request.method == 'POST':
        formset = StaffSalaryPaymentFormSet(request.POST)

        payment_source = request.POST.get('payment_source')
        if not payment_source or payment_source not in ['cash', 'bank']:
            messages.error(request, "Select a valid payment source (cash or bank).")
            return redirect('salary_payment_create')

        if formset.is_valid():
            total_payment_sum = 0
            payments = []

            with transaction.atomic():
                for form in formset:
                    cleaned = form.cleaned_data
                    staff = cleaned['staff']
                    salary = cleaned['salary']
                    bonus = cleaned['bonus']
                    deduction = cleaned['deduction']
                    target_bonus = cleaned['target_bonus']
                    total_payment = salary + bonus + target_bonus - deduction

                    payments.append(StaffSalaryPaymentModel(
                        staff=staff,
                        salary=salary,
                        bonus=bonus,
                        deduction=deduction,
                        target_bonus=target_bonus,
                        total_payment=total_payment,
                        month=current_month,
                        created_by=request.user
                    ))

                    total_payment_sum += total_payment

                # Check if site setting balance is sufficient
                if payment_source == 'cash':
                    if site_setting.petty_cash_balance < float(total_payment_sum):
                        messages.error(request, "Insufficient petty cash balance.")
                        return redirect('salary_payment_create')
                    site_setting.petty_cash_balance -= float(total_payment_sum)
                    site_setting.save(update_fields=['petty_cash_balance'])

                elif payment_source == 'bank':
                    if site_setting.balance < float(total_payment_sum):
                        messages.error(request, "Insufficient bank balance.")
                        return redirect('salary_payment_create')
                    site_setting.balance -= float(total_payment_sum)
                    site_setting.save(update_fields=['balance'])

                # Save all payments
                StaffSalaryPaymentModel.objects.bulk_create(payments)

                # Create summary
                StaffSalarySummaryModel.objects.create(
                    total_staff=len(payments),
                    total_bonus=sum(p.bonus for p in payments),
                    total_deduction=sum(p.deduction for p in payments),
                    total_payment=total_payment_sum,
                    payment_source=payment_source,
                    month=current_month,
                    created_by=request.user
                )

                # Log activity
                log_html = f"""
                <div class='bg-success text-white p-2' style='border-radius: 5px;'>
                    <p>
                        <b>{escape(request.user.get_full_name())}</b> paid salary for
                        <b>{len(payments)}</b> staff for <b>{current_month.strftime('%B %Y')}</b><br>
                        Total Paid: ₦{total_payment_sum:,.2f} from <b>{payment_source.upper()}</b>
                        <span class='float-end'>{now():%Y-%m-%d %H:%M:%S}</span>
                    </p>
                </div>
                """
                ActivityLogModel.objects.create(
                    log=log_html,
                    user=request.user,
                    category='finance',
                    keywords='salary__monthly__payment'
                )

                messages.success(request, f"Salary payments created for {current_month.strftime('%B %Y')}.")
                return redirect('salary_payment_view', month=current_month.strftime('%Y-%m-%d'))

        else:
            messages.error(request, "Please correct the errors in the form.")
            return render(request, 'finance/salary_payment/create.html', {
                'formset': formset,
                'month': current_month,
                'staff_list': StaffModel.objects.all()
            })

    # --- GET request ---
    initial_data = []
    for profile in staff_salaries:
        staff = profile.staff
        bonus = profile.total_bonus_for_month(current_month)
        deduction = profile.total_deduction_for_month(current_month)

        # Target bonus logic
        target_bonus = Decimal('0.00')
        if getattr(staff, 'is_driver', False):
            target = (
                staff.crate_target_for_bonus
                if staff.crate_target_for_bonus and staff.crate_target_for_bonus > 0
                else site_setting.crate_target_for_bonus
            )
            if target and target > 0:
                total_items = SaleItemModel.objects.filter(
                    sale__driver=staff,
                    sale__status='confirmed',
                    sale__sale_date__month=current_month.month,
                    sale__sale_date__year=current_month.year,
                ).aggregate(total=Sum('quantity'))['total'] or 0

                if total_items > target:
                    extra = total_items - target
                    target_bonus = Decimal(extra) * Decimal(site_setting.bonus_amount_per_crate or 0)

        total_payment = profile.salary + bonus + target_bonus - deduction

        initial_data.append({
            'staff': staff,
            'salary': profile.salary,
            'bonus': bonus,
            'deduction': deduction,
            'target_bonus': target_bonus,
            'total_payment': total_payment,
            'month': current_month,

        })

    formset = StaffSalaryPaymentFormSet(queryset=StaffSalaryPaymentModel.objects.none(), initial=initial_data)

    return render(request, 'finance/salary_payment/create.html', {
        'formset': formset,
        'month': current_month,
        'staff_list': StaffModel.objects.all(),
        'cash_balance': site_setting.cash_balance or 0,
        'bank_balance': site_setting.balance or 0,
        'site_setting': site_setting
    })


@login_required
@permission_required("finance.add_staffsalarypaymentmodel", raise_exception=True)
def salary_payment_view(request, month=None):
    # Parse month (string 'YYYY-MM-DD') into date

    if not month:
        month = request.GET.get('month')

        # Still not provided? Use current month
    if not month:
        month_date = timezone.now().date().replace(day=1)
    else:
        # Accept both YYYY-MM and YYYY-MM-DD
        try:
            if len(month) == 7:  # e.g. '2025-06'
                month_date = datetime.strptime(month, '%Y-%m').date().replace(day=1)
            else:  # fallback for full date
                month_date = datetime.strptime(month, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, 'Invalid month format. Use YYYY-MM or YYYY-MM-DD.')
            return redirect('salary_payment_index')  # or safe fallback

    payments = StaffSalaryPaymentModel.objects.filter(month=month_date).select_related('staff').order_by('staff__full_name')

    # Calculate totals for footer
    total_salary = sum(p.salary for p in payments)
    total_bonus = sum(p.bonus for p in payments)
    total_target_bonus = sum(p.target_bonus for p in payments)
    total_deduction = sum(p.deduction for p in payments)
    grand_total = sum(p.total_payment for p in payments)

    context = {
        'payments': payments,
        'payment_summary': StaffSalarySummaryModel.objects.filter(month=month_date).first(),
        'month': month_date,
        'total_salary': total_salary,
        'total_bonus': total_bonus,
        'total_target_bonus': total_target_bonus,
        'total_deduction': total_deduction,
        'grand_total': grand_total,
    }
    return render(request, 'finance/salary_payment/index.html', context)


class WalletDashboardView(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = 'finance/wallet/dashboard.html'
    permission_required = 'finance.add_cashtransfermodel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        settings = SiteSettingModel.objects.first()
        staff_wallets = StaffWalletModel.objects.select_related('staff').all()

        context['form'] = CashTransferForm()
        context['staff_wallets'] = staff_wallets
        context['bank_balance'] = settings.balance
        context['cash_balance'] = settings.cash_balance
        context['petty_cash_balance'] = settings.petty_cash_balance
        context['vendor_balance'] = SupplierModel.objects.aggregate(total=Sum('balance'))['total'] or 0.0
        context['total_staff_balance'] = sum(w.balance for w in staff_wallets)
        context['supplier_list'] = SupplierModel.objects.all()
        context['total_customer_debt'] = CustomerWalletModel.objects.aggregate(
            total=Sum('balance')
        )['total'] or 0.0

        context['total_balance'] = (
                Decimal(str(context['bank_balance'])) +
                Decimal(str(context['cash_balance'])) +
                Decimal(str(context['petty_cash_balance'])) +
                Decimal(str(context['vendor_balance'])) +
                Decimal(str(context['total_staff_balance'])) +
                Decimal(str(context['total_customer_debt']))
        )

        return context

    def post(self, request, *args, **kwargs):
        form = CashTransferForm(request.POST)
        if form.is_valid():
            transfer = form.save(commit=False)
            transfer.created_by = request.user
            transfer.source, transfer.destination = self._map_transfer(transfer.transfer_type)
            transfer.save()
            messages.success(request, "Transfer completed successfully.")
        else:
            for error in form.non_field_errors():
                messages.error(request, error)

            for field, errors in form.errors.items():
                if field != '__all__':
                    label = form.fields[field].label
                    for error in errors:
                        messages.error(request, f"{label}: {error}")

            return self.render_to_response(self.get_context_data(form=form))

        return redirect('wallet_dashboard')

    def _map_transfer(self, transfer_type):
        return {
            'staff_to_cash': ('staff', 'cash'),
            'staff_to_bank': ('staff', 'bank'),
            'cash_to_bank': ('cash', 'bank'),
            'bank_to_cash': ('bank', 'cash'),
            'bank_to_petty': ('bank', 'petty'),
            'cash_to_petty': ('cash', 'petty'),
            'bank_to_supplier': ('bank', 'supplier'),
            'cash_to_supplier': ('cash', 'supplier'),
            'adjustment_add': ('bank', 'bank'),
            'adjustment_subtract': ('bank', 'bank'),
        }.get(transfer_type, ('', ''))


class BankAdjustmentView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'finance.add_cashtransfermodel'

    def post(self, request):
        adjustment_type = request.POST.get('adjustment_type')
        amount = request.POST.get('amount')
        note = request.POST.get('note', '').strip()

        # Field-level validation
        has_error = False
        if not adjustment_type:
            messages.error(request, "Adjustment type is required.")
            has_error = True

        if not amount:
            messages.error(request, "Amount is required.")
            has_error = True
        else:
            try:
                amount = float(amount)
                if amount <= 0:
                    messages.error(request, "Amount must be greater than 0.")
                    has_error = True
            except ValueError:
                messages.error(request, "Amount must be a valid number.")
                has_error = True

        if not note:
            messages.error(request, "Adjustment note is required.")
            has_error = True

        if has_error:
            return redirect('wallet_dashboard')

        settings = SiteSettingModel.objects.first()

        if adjustment_type == "add":
            messages.success(request, f"Bank account adjusted ↑ by ₦{amount:,.2f}")
        elif adjustment_type == "subtract":
            if amount > settings.balance:
                messages.error(request, "Cannot subtract more than current bank balance.")
                return redirect('wallet_dashboard')
            messages.success(request, f"Bank account adjusted ↓ by ₦{amount:,.2f}")
        else:
            messages.error(request, "Invalid adjustment type.")
            return redirect('wallet_dashboard')

        settings.save()

        CashTransferModel.objects.create(
            source='bank',
            destination='bank',
            amount=amount,
            transfer_type=f'adjustment_{adjustment_type}',
            comment=note,
            created_by=request.user
        )

        return redirect('wallet_dashboard')


@login_required
@permission_required("sale.add_customerdebtrepaymentmodel", raise_exception=True)
def debtors_overview_view(request):
    # --- Monetary Debtors ---
    monetary_debtors = (
        CustomerWalletModel.objects
        .filter(balance__gt=Decimal('0.00'))
        .select_related('customer')
        .order_by('-balance')
    )

    # --- Crate Debtors ---
    crate_debtors_raw = (
        CustomerCrateDebtModel.objects
        .values('customer__id', 'customer__full_name')
        .annotate(total_crate_debt=Sum('crate'))
        .filter(total_crate_debt__gt=Decimal('0.00'))
        .order_by('-total_crate_debt')
    )

    context = {
        'monetary_debtors': monetary_debtors,
        'crate_debtors': crate_debtors_raw,
        'title': 'Customer Debtors Overview',
    }

    return render(request, 'finance/debtor/index.html', context)


def get_wallet_choices():
    """Builds a dynamic list of all wallets."""
    wallets = [
        ('bank', 'Main Bank Account'),
        ('cash', 'Main Office Cash'),
        ('petty', 'Main Petty Cash'),
    ]

    # Add staff wallets
    staff_wallets = StaffModel.objects.filter(wallet__isnull=False).select_related('wallet')
    wallets.extend([
        (f'staff_{s.id}', f'Staff: {s.full_name} (Balance: ₦{s.wallet.balance:,.2f})')
        for s in staff_wallets
    ])

    # Add supplier wallets (accounts payable)
    suppliers = SupplierModel.objects.all()
    wallets.extend([
        (f'supplier_{s.id}', f'Supplier: {s.name} (Balance: ₦{s.balance:,.2f})')
        for s in suppliers
    ])

    return wallets


def get_wallet_statement(wallet_id, start_date, end_date):
    """
    Fetches, combines, and processes transactions for the selected wallet.
    """
    transactions = []

    # Combine date and time for precise filtering
    start_dt = LOCAL_TZ.localize(datetime.combine(start_date, time.min))
    end_dt = LOCAL_TZ.localize(datetime.combine(end_date, time.max))

    # --- 1. Get Opening Balance ---
    # We calculate this by summing all transactions *before* the start_date
    # This is a simplified approach; a more robust way would be to run the full query
    # on all history, but that can be slow. We'll calculate it from the transactions.

    # --- 2. Gather All Transactions in Date Range ---

    # Universal IN: Customer Debt Repayments
    if wallet_id in ['bank', 'cash'] or wallet_id.startswith('staff_'):
        repayments = CustomerDebtRepaymentModel.objects.filter(
            created_at__range=(start_dt, end_dt)
        ).select_related('customer')

        if wallet_id == 'bank':
            repayments = repayments.filter(payment_method='bank')
        elif wallet_id == 'cash':
            repayments = repayments.filter(payment_method='cash')
        elif wallet_id.startswith('staff_'):
            staff_id = int(wallet_id.split('_')[1])
            repayments = repayments.filter(payment_method='driver', driver_id=staff_id)
        else:
            repayments = repayments.none()

        transactions.extend([
            {
                'date': t.created_at,
                'description': f"Debt Repayment from {t.customer.full_name}",
                'credit': t.amount_paid,
                'debit': Decimal('0.00'),
                'obj': t
            } for t in repayments
        ])

    # Universal IN: Sales
    if wallet_id in ['bank', 'cash'] or wallet_id.startswith('staff_'):
        sales = SaleModel.objects.filter(
            status='confirmed',
            sale_date__range=(start_dt, end_dt),
            total_amount_paid__gt=0
        ).select_related('customer')

        if wallet_id == 'bank':
            sales = sales.filter(payment_destination='bank')
        elif wallet_id == 'cash':
            sales = sales.filter(payment_destination='cash')
        elif wallet_id.startswith('staff_'):
            staff_id = int(wallet_id.split('_')[1])
            sales = sales.filter(payment_destination='driver', driver_id=staff_id)
        else:
            sales = sales.none()

        transactions.extend([
            {
                'date': t.sale_date,
                'description': f"Sale #{t.transaction_id} (Customer: {t.customer.full_name if t.customer else 'N/A'})",
                'credit': t.total_amount_paid,
                'debit': Decimal('0.00'),
                'obj': t
            } for t in sales
        ])

    # Universal IN: Crate Returns for Cash (Customer PAYS us)
    if wallet_id in ['bank', 'cash'] or wallet_id.startswith('staff_'):
        crate_returns = CustomerCrateReturnModel.objects.filter(
            return_method='cash',
            created_at__range=(start_dt, end_dt)
        ).select_related('customer', 'driver')

        if wallet_id == 'bank':
            crate_returns = crate_returns.filter(payment_method='bank')
        elif wallet_id == 'cash':
            crate_returns = crate_returns.filter(payment_method='cash')
        elif wallet_id.startswith('staff_'):
            staff_id = int(wallet_id.split('_')[1])
            crate_returns = crate_returns.filter(payment_method='driver', driver_id=staff_id)
        else:
            crate_returns = crate_returns.none()

        transactions.extend([
            {
                'date': t.created_at,
                'description': f"Cash for Crates from {t.customer.full_name}",
                'credit': t.amount_paid,
                'debit': Decimal('0.00'),
                'obj': t
            } for t in crate_returns
        ])

    # Universal OUT: Expenses
    if wallet_id in ['bank', 'petty']:
        expenses = ExpenseModel.objects.filter(
            date__range=(start_date, end_date)  # Expense uses DateField
        ).select_related('type')

        if wallet_id == 'bank':
            expenses = expenses.filter(payment_source='ACCOUNT_BALANCE')
        elif wallet_id == 'petty':
            expenses = expenses.filter(payment_source='PETTY_CASH')
        else:
            expenses = expenses.none()

        transactions.extend([
            {
                'date': datetime.combine(t.date, time.min).astimezone(LOCAL_TZ),
                'description': f"Expense: {t.type.name} ({t.remark or 'N/A'})",
                'credit': Decimal('0.00'),
                'debit': t.amount,
                'obj': t
            } for t in expenses
        ])

    # Universal OUT: Salary Payments
    if wallet_id in ['bank', 'petty']:  # Note: Your code uses 'petty_cash_balance' for 'cash' source
        salaries = StaffSalarySummaryModel.objects.filter(
            month__range=(start_date, end_date)
        )

        if wallet_id == 'bank':
            salaries = salaries.filter(payment_source='bank')
        elif wallet_id == 'petty':
            salaries = salaries.filter(payment_source='cash')  # This maps to petty_cash_balance
        else:
            salaries = salaries.none()

        transactions.extend([
            {
                'date': datetime.combine(t.month, time.min).astimezone(LOCAL_TZ),
                'description': f"Salary Payment for {t.month.strftime('%B %Y')}",
                'credit': Decimal('0.00'),
                'debit': t.total_payment,
                'obj': t
            } for t in salaries
        ])

    # Universal IN/OUT: Cash Transfers
    transfers = CashTransferModel.objects.filter(
        created_at__range=(start_dt, end_dt)
    ).select_related('staff', 'supplier')

    if wallet_id == 'bank':
        transfers = transfers.filter(Q(source='bank') | Q(destination='bank'))
    elif wallet_id == 'cash':
        transfers = transfers.filter(Q(source='cash') | Q(destination='cash'))
    elif wallet_id == 'petty':
        transfers = transfers.filter(Q(source='petty') | Q(destination='petty'))
    elif wallet_id.startswith('staff_'):
        staff_id = int(wallet_id.split('_')[1])
        transfers = transfers.filter(Q(source='staff', staff_id=staff_id) | Q(destination='staff', staff_id=staff_id))
    elif wallet_id.startswith('supplier_'):
        supplier_id = int(wallet_id.split('_')[1])
        transfers = transfers.filter(
            Q(source='supplier', supplier_id=supplier_id) | Q(destination='supplier', supplier_id=supplier_id))
    else:
        transfers = transfers.none()

    for t in transfers:
        credit, debit = Decimal('0.00'), Decimal('0.00')
        amount = Decimal(str(t.amount))

        if t.transfer_type.startswith('adjustment_add'):
            if wallet_id == 'bank': credit = amount
        elif t.transfer_type.startswith('adjustment_subtract'):
            if wallet_id == 'bank': debit = amount
        elif t.destination == wallet_id:
            credit = amount
        elif t.source == wallet_id:
            debit = amount
        elif wallet_id.startswith('staff_') and t.destination == 'staff' and t.staff_id == int(wallet_id.split('_')[1]):
            credit = amount
        elif wallet_id.startswith('staff_') and t.source == 'staff' and t.staff_id == int(wallet_id.split('_')[1]):
            debit = amount
        elif wallet_id.startswith('supplier_') and t.destination == 'supplier' and t.supplier_id == int(
                wallet_id.split('_')[1]):
            credit = amount  # Credit to supplier (we paid them)
        elif wallet_id.startswith('supplier_') and t.source == 'supplier' and t.supplier_id == int(
                wallet_id.split('_')[1]):
            debit = amount  # Debit from supplier

        transactions.append({
            'date': t.created_at,
            'description': t.get_transfer_type_display() + (f" ({t.comment})" if t.comment else ""),
            'credit': credit,
            'debit': debit,
            'obj': t
        })

    # Special: Supplier Debits (Stock Purchases)
    if wallet_id.startswith('supplier_'):
        supplier_id = int(wallet_id.split('_')[1])
        purchases = StockInSummaryModel.objects.filter(
            status='confirmed',
            supplier_id=supplier_id,
            date__range=(start_date, end_date)
        ).annotate(
            total_cost=Sum(F('products__quantity_added') * F('products__unit_cost_price'), output_field=DecimalField())
        )

        transactions.extend([
            {
                'date': datetime.combine(t.date, time.min).astimezone(LOCAL_TZ),
                'description': f"Stock Purchase Receipt #{t.pk}",
                'credit': Decimal('0.00'),  # Purchase is a DEBIT from supplier balance
                'debit': t.total_cost or Decimal('0.00'),
                'obj': t
            } for t in purchases
        ])

    # --- 3. Sort by Date ---
    transactions.sort(key=lambda x: x['date'])

    # --- 4. Calculate Opening & Running Balance ---
    # This is complex. For now, we'll get the *current* balance and work backwards.
    # A full opening balance requires summing all tx *before* start_date.

    current_balance = Decimal('0.00')
    settings = SiteSettingModel.objects.first()
    if settings:
        if wallet_id == 'bank':
            current_balance = Decimal(str(settings.balance))
        elif wallet_id == 'cash':
            current_balance = Decimal(str(settings.cash_balance))
        elif wallet_id == 'petty':
            current_balance = Decimal(str(settings.petty_cash_balance))

    if wallet_id.startswith('staff_'):
        try:
            staff_id = int(wallet_id.split('_')[1])
            current_balance = Decimal(str(StaffWalletModel.objects.get(staff_id=staff_id).balance))
        except StaffWalletModel.DoesNotExist:
            current_balance = Decimal('0.00')

    if wallet_id.startswith('supplier_'):
        try:
            supplier_id = int(wallet_id.split('_')[1])
            current_balance = Decimal(str(SupplierModel.objects.get(id=supplier_id).balance))
        except SupplierModel.DoesNotExist:
            current_balance = Decimal('0.00')

    # Process list in reverse to get opening balance
    closing_balance = current_balance
    running_balance = closing_balance

    # We must iterate backwards to find the opening balance
    for tx in reversed(transactions):
        tx['running_balance'] = running_balance
        running_balance -= (tx['credit'] - tx['debit'])

    opening_balance = running_balance

    return transactions, opening_balance, closing_balance


class WalletStatementView(LoginRequiredMixin, TemplateView):
    template_name = 'finance/wallet/statement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request

        # Get query params
        today = datetime.now().date()
        default_start = today.replace(day=1)

        wallet_id = request.GET.get('wallet_id')
        start_date_str = request.GET.get('start_date', default_start.isoformat())
        end_date_str = request.GET.get('end_date', today.isoformat())

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            start_date = default_start
            end_date = today

        context['wallet_choices'] = get_wallet_choices()
        context['selected_wallet'] = wallet_id
        context['start_date'] = start_date
        context['end_date'] = end_date

        if wallet_id:
            transactions, opening, closing = get_wallet_statement(wallet_id, start_date, end_date)
            context['transactions'] = transactions
            context['opening_balance'] = opening
            context['closing_balance'] = closing

        return context

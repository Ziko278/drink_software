import json
import logging
import random

from django.forms import modelformset_factory
from django.utils.html import escape
from django.utils.timezone import localtime, now
from django.views import View
from pytz import timezone as pytz_timezone
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

from sale.models import SaleModel, SaleItemModel, CustomerWalletModel, CustomerCrateDebtModel

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


class ExpenseCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    model = ExpenseModel
    permission_required = 'finance.add_expensemodel'
    form_class = ExpenseForm
    success_message = 'Expense Added Successfully'
    template_name = 'finance/expense/index.html'

    def get_success_url(self):
        return reverse('expense_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())

    def form_valid(self, form):
        site_setting = SiteSettingModel.objects.first()
        expense_amount = form.cleaned_data['amount']

        # Check if there is enough petty cash
        if site_setting.petty_cash_balance < float(expense_amount):
            messages.error(self.request, f"Insufficient petty cash. Available: ₦{site_setting.petty_cash_balance:,.2f}")
            return redirect(self.get_success_url())

        # Deduct amount from petty cash
        site_setting.petty_cash_balance -= float(expense_amount)
        site_setting.save(update_fields=['petty_cash_balance'])

        # Save the expense
        form.instance.created_by = self.request.user
        response = super().form_valid(form)

        # Log activity
        staff = get_staff_instance(self.request.user)
        expense = form.instance
        local_time = localtime(now(), pytz_timezone('Africa/Lagos')).strftime("%Y-%m-%d %H:%M:%S")
        staff_url = reverse('staff_detail', kwargs={'pk': staff.pk}) if staff else "#"

        log_html = f"""
        <div class='bg-danger text-white p-2' style='border-radius:5px;'>
            <p>
                <b><a href="{staff_url}" class="text-white text-decoration-underline">
                    {escape(staff.full_name.title())}
                </a></b> recorded an expense of 
                <b>₦{expense.amount:,.2f}</b> under <b>{escape(expense.type.name)}</b>.<br>
                Remark: {escape(expense.remark or "N/A")}
                <span class='float-end'>{local_time}</span>
            </p>
        </div>
        """

        ActivityLogModel.objects.create(
            log=log_html,
            user=self.request.user,
            category='finance',
            keywords='finance__expense_created'
        )

        return response


class ExpenseListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ExpenseModel
    permission_required = 'finance.add_expensemodel'
    template_name = 'finance/expense/index.html'
    context_object_name = "expense_list"

    def get_queryset(self):
        return ExpenseModel.objects.select_related('type').order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ExpenseForm()
        context['site_setting'] = SiteSettingModel.objects.first()
        return context


class ExpenseUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ExpenseModel
    permission_required = 'finance.add_expensemodel'
    form_class = ExpenseForm
    success_message = 'Expense Updated Successfully'
    template_name = 'finance/expense/index.html'

    def get_success_url(self):
        return reverse('expense_index')

    def dispatch(self, *args, **kwargs):
        if self.request.method == 'GET':
            return redirect(self.get_success_url())
        return super().dispatch(*args, **kwargs)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{form.fields[field].label}: {error}")
        return redirect(self.get_success_url())

    def form_valid(self, form):
        site_setting = SiteSettingModel.objects.first()
        staff = get_staff_instance(self.request.user)
        old_expense = self.get_object()
        new_amount = form.cleaned_data['amount']
        old_amount = old_expense.amount
        difference = new_amount - old_amount

        # Restrict update if older than 3 hours
        if now() - old_expense.created_at > timedelta(hours=3):
            messages.error(self.request, "You can only edit an expense within 3 hours of creation.")
            return redirect(self.get_success_url())

        # If increasing amount, validate petty cash
        if difference > 0 and site_setting.petty_cash_balance < float(difference):
            messages.error(self.request, f"Not enough petty cash to increase amount by ₦{difference:,.2f}")
            return redirect(self.get_success_url())

        # Update petty cash accordingly
        site_setting.petty_cash_balance -= float(difference)  # works even if difference is negative (refund)
        site_setting.save(update_fields=['petty_cash_balance'])

        response = super().form_valid(form)

        # Log
        local_time = localtime(now(), pytz_timezone('Africa/Lagos')).strftime("%Y-%m-%d %H:%M:%S")
        staff_url = reverse('staff_detail', kwargs={'pk': staff.pk}) if staff else "#"

        if difference > 0:
            note = f"and an extra ₦{difference:,.2f} was deducted from petty cash"
            color = 'warning'
        elif difference < 0:
            note = f"and ₦{abs(difference):,.2f} was refunded to petty cash"
            color = 'info'
        else:
            note = "with no change in amount"
            color = 'secondary'

        log_html = f"""
        <div class='bg-{color} text-white p-2' style='border-radius:5px;'>
            <p>
                <b><a href="{staff_url}" class="text-white text-decoration-underline">
                    {escape(staff.full_name.title())}
                </a></b> updated an expense from 
                <b>₦{old_amount:,.2f}</b> to <b>₦{new_amount:,.2f}</b> {note}.<br>
                <span class='float-end'>{local_time}</span>
            </p>
        </div>
        """

        ActivityLogModel.objects.create(
            log=log_html,
            user=self.request.user,
            category='finance',
            keywords='finance__expense_updated'
        )

        return response


class ExpenseDeleteView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    model = ExpenseModel
    permission_required = 'finance.add_expensemodel'
    success_message = 'Expense deleted successfully.'
    template_name = 'finance/expense/delete.html'
    context_object_name = "expense"

    def get_success_url(self):
        return reverse('expense_index')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        expense = self.object
        site_setting = SiteSettingModel.objects.first()

        # ✅ 3-hour restriction
        if (now() - expense.created_at).total_seconds() > 3 * 3600:
            messages.error(request, "This expense was recorded more than 3 hours ago and cannot be deleted.")
            return redirect(self.get_success_url())

        # ✅ Reverse amount to petty cash
        site_setting.petty_cash_balance += float(expense.amount)
        site_setting.save(update_fields=['petty_cash_balance'])

        # ✅ Log activity
        staff_member = get_staff_instance(request.user)
        staff_url = reverse('staff_detail', kwargs={'pk': staff_member.pk}) if staff_member else '#'
        timestamp = localtime(now(), pytz_timezone('Africa/Lagos')).strftime('%Y-%m-%d %H:%M:%S')

        log_html = f"""
        <div class='bg-danger text-white p-2' style='border-radius:5px;'>
            <p>
                <b><a href="{staff_url}" class="text-white text-decoration-underline">{escape(staff_member.full_name)}</a></b>
                deleted an expense of <b>₦{expense.amount:.2f}</b> for type <b>{escape(expense.type.name)}</b>.<br>
                ₦{expense.amount:.2f} was refunded to petty cash.<br>
                <span class='float-end'>{timestamp}</span>
            </p>
        </div>
        """

        ActivityLogModel.objects.create(
            log=log_html,
            user=request.user,
            category='finance',
            keywords='expense__delete'
        )

        return super().post(request, *args, **kwargs)


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

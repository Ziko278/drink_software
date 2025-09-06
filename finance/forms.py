from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from django.utils import timezone

from human_resource.models import StaffModel
from inventory.models import SupplierModel
from .models import (
    ExpenseModel, ExpenseTypeModel,
    StaffSalaryModel, StaffSalarySummaryModel,
    StaffBonusModel, StaffDeductionModel,
    StaffSalaryPaymentModel, CashTransferModel
)
import calendar


class BaseStyledModelForm(forms.ModelForm):
    """Reusable base form to style form fields."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Don't apply form-control to radio buttons
            if not isinstance(self.fields[field].widget, forms.RadioSelect):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

class ExpenseTypeForm(BaseStyledModelForm):
    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        qs = ExpenseTypeModel.objects.filter(name__iexact=name)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("Expense type with this name already exists.")
        return name

    class Meta:
        model = ExpenseTypeModel
        fields = ['name', 'description']


class ExpenseForm(BaseStyledModelForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount and amount <= 0:
            raise ValidationError("Amount must be greater than zero.")
        return amount

    class Meta:
        model = ExpenseModel
        # ✅ Add 'payment_source' to the fields list
        fields = ['type', 'amount', 'payment_source', 'remark']
        widgets = {
            # This ensures it renders as radio buttons in the template
            'payment_source': forms.RadioSelect,
        }


class StaffSalaryForm(BaseStyledModelForm):
    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary < 0:
            raise ValidationError("Salary cannot be negative.")
        return salary

    class Meta:
        model = StaffSalaryModel
        fields = ['staff', 'salary', 'account_name', 'account_number', 'bank']


class StaffSalarySummaryForm(BaseStyledModelForm):
    class Meta:
        model = StaffSalarySummaryModel
        fields = ['total_staff', 'total_bonus', 'total_deduction', 'total_payment', 'month', 'payment_source']


class StaffBonusForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today = timezone.now().date()
        first_day = today.replace(day=1)
        last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])

        self.fields['date'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': first_day.isoformat(),
                'max': last_day.isoformat(),
                'autocomplete': 'off'
            }
        )

        # Style other fields
        for field in self.fields:
            if field != 'date':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    def clean_bonus(self):
        bonus = self.cleaned_data['bonus']
        if bonus <= 0:
            raise ValidationError("Bonus must be greater than zero.")
        return bonus

    def clean_date(self):
        date = self.cleaned_data['date']
        today = timezone.now().date()
        if date.month != today.month or date.year != today.year:
            raise ValidationError("Date must be within the current month.")
        return date

    class Meta:
        model = StaffBonusModel
        fields = ['staff', 'bonus', 'note', 'date']


class StaffDeductionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        today = timezone.now().date()
        first_day = today.replace(day=1)
        last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])

        self.fields['date'].widget = forms.DateInput(
            attrs={
                'type': 'date',
                'class': 'form-control',
                'min': first_day.isoformat(),
                'max': last_day.isoformat(),
                'autocomplete': 'off'
            }
        )

        # Style other fields
        for field in self.fields:
            if field != 'date':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    def clean_deduction(self):
        deduction = self.cleaned_data['deduction']
        if deduction <= 0:
            raise ValidationError("Deduction must be greater than zero.")
        return deduction

    def clean_date(self):
        date = self.cleaned_data['date']
        today = timezone.now().date()
        if date.month != today.month or date.year != today.year:
            raise ValidationError("Date must be within the current month.")
        return date

    class Meta:
        model = StaffDeductionModel
        fields = ['staff', 'deduction', 'note', 'date']


class StaffSalaryPaymentForm(BaseStyledModelForm):
    staff_name = forms.CharField(required=False, disabled=True, label="Staff")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['staff'].readonly = True

        # Disable other fields
        for field_name in ['salary', 'bonus', 'deduction', 'total_payment', 'month']:
            self.fields[field_name].widget.attrs['readonly'] = True

        # Set initial staff_name from initial data if exists
        if 'initial' in kwargs and 'staff_name' in kwargs['initial']:
            self.fields['staff_name'].initial = kwargs['initial']['staff_name']

    def clean(self):
        cleaned_data = super().clean()
        salary = cleaned_data.get("salary", 0)
        bonus = cleaned_data.get("bonus", 0)
        deduction = cleaned_data.get("deduction", 0)
        target_bonus = cleaned_data.get("target_bonus", 0)
        total = cleaned_data.get("total_payment", 0)

        expected_total = salary + bonus + target_bonus - deduction
        if total != expected_total:
            raise ValidationError(
                f"Total payment must equal salary + bonus + target_bonus - deduction (₦{expected_total})."
            )

        return cleaned_data

    class Meta:
        model = StaffSalaryPaymentModel
        fields = [
            'staff',
            'salary',
            'bonus',
            'deduction',
            'target_bonus',
            'total_payment',
            'month',
        ]


StaffSalaryPaymentFormSet = modelformset_factory(
    StaffSalaryPaymentModel,
    form=StaffSalaryPaymentForm,
    extra=0,
    can_delete=False,
)


class CashTransferForm(forms.ModelForm):
    class Meta:
        model = CashTransferModel
        fields = [
            'transfer_type',
            'staff',
            'supplier',
            'amount',
            'comment',
            'source',
            'destination'
        ]
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

        self.fields['staff'].required = False
        self.fields['staff'].queryset = StaffModel.objects.filter(wallet__balance__gt=0)

        self.fields['supplier'].required = False
        self.fields['supplier'].queryset = SupplierModel.objects.all()


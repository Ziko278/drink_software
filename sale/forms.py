from django import forms
from django.forms import ModelForm, modelformset_factory, Select, TextInput, CheckboxInput
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal

from human_resource.models import StaffModel
# --- IMPORTANT: Adjust these imports based on your app structure ---
# Make sure your sale models and necessary inventory models are correctly imported
from sale.models import CustomerModel, SaleModel, SaleItemModel, ReturnModel, SaleCategoryEmpty, \
    CustomerDebtRepaymentModel, CustomerCrateReturnModel
from inventory.models import ProductModel, \
    CategoryModel  # ProductModel needed for SaleItemForm, CategoryModel for crate debt if applicable


# --- End of important imports ---


# --- Customer Form ---
class CustomerForm(ModelForm):
    """ Form for creating/editing CustomerModel. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        qs = CustomerModel.objects.filter(mobile=mobile)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError("A customer with this mobile number already exists.")
        return mobile

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Validate uniqueness only if email is provided (since it's nullable)
        if email:
            qs = CustomerModel.objects.filter(email__iexact=email)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise ValidationError("A customer with this email already exists.")
        return email

    class Meta:
        model = CustomerModel
        fields = '__all__'
        # Widgets are mostly handled in __init__
        # 'email' field uses TextInput by default, which is fine with 'form-control' class


class CustomerDebtRepaymentForm(forms.ModelForm):
    class Meta:
        model = CustomerDebtRepaymentModel
        fields = ['customer', 'amount_paid', 'driver', 'payment_method', 'note']

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.01', 'min': '0.01'
            }),
            'payment_method': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        labels = {
            'customer': 'Customer',
            'amount_paid': 'Amount Paid',
            'payment_method': 'Payment Method',
            'note': 'Optional Note',
        }


class CustomerCrateReturnForm(forms.ModelForm):
    class Meta:
        model = CustomerCrateReturnModel
        fields = ['customer', 'category', 'crates_returned', 'note', 'return_method', 'amount_paid', 'payment_method', 'driver']

        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'crates_returned': forms.NumberInput(attrs={
                'class': 'form-control', 'step': '0.01', 'min': '0.01'
            }),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        labels = {
            'customer': 'Customer',
            'category': 'Product Category',
            'crates_returned': 'Number of Crates Returned',
            'note': 'Optional Note',
        }


class SaleForm(forms.ModelForm):
    """Form for the main SaleModel (transaction header)."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['driver'].queryset = StaffModel.objects.filter(is_driver=True)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

        if not self.instance.pk:
            self.initial['sale_date'] = timezone.now().strftime('%Y-%m-%d')
            self.initial['payment_status'] = 'none'

        # Hide system-calculated fields
        for field_name in ['payment_status', 'total_amount', 'total_amount_paid', 'total_amount_left']:
            if field_name in self.fields:
                self.fields[field_name].widget = forms.HiddenInput()
                self.fields[field_name].required = False

    class Meta:
        model = SaleModel
        fields = [
            'sale_date', 'customer', 'driver', 'status',
            'payment_status', 'delivery_status', 'payment_destination',
            'total_amount', 'total_amount_paid', 'total_amount_left'
        ]
        widgets = {
            'sale_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'sale_date': 'Sale Date',
            'total_amount_paid': 'Amount Paid',
            'total_amount_left': 'Amount Left',
        }


class SaleItemForm(forms.ModelForm):
    """Form for a single product in the sale."""

    class Meta:
        model = SaleItemModel
        fields = ['product', 'quantity', 'unit_price']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control product-select'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01'}),
        }
        labels = {
            'product': 'Product',
            'quantity': 'Quantity Sold',
            'unit_price': 'Unit Selling Price',
        }

    def clean(self):
        cleaned_data = super().clean()
        if not self.cleaned_data.get('DELETE', False):
            product = cleaned_data.get('product')
            quantity = cleaned_data.get('quantity')
            unit_price = cleaned_data.get('unit_price')

            if product:
                if quantity is None or quantity <= Decimal('0.00'):
                    self.add_error('quantity', 'Quantity must be greater than zero.')
                if unit_price is None or unit_price <= Decimal('0.00'):
                    self.add_error('unit_price', 'Unit price must be greater than zero.')
        return cleaned_data


class SaleCategoryEmptyForm(forms.ModelForm):
    class Meta:
        model = SaleCategoryEmpty
        fields = ['category', 'empty_expected', 'empty_brought', 'empty_owed']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'empty_expected': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': True}),
            'empty_brought': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'empty_owed': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'readonly': True}),
        }
        labels = {
            'category': 'Category',
            'empty_expected': 'Expected Empty Crates',
            'empty_brought': 'Empty Crates Brought',
            'empty_owed': 'Empty Crates Owed',
        }

    def clean(self):
        cleaned_data = super().clean()
        expected = cleaned_data.get('empty_expected') or Decimal('0.00')
        brought = cleaned_data.get('empty_brought') or Decimal('0.00')
        owed = expected - brought

        if owed < 0:
            self.add_error('empty_brought', 'Crates brought cannot exceed expected crates.')

        cleaned_data['empty_owed'] = owed
        return cleaned_data


SaleItemCreateFormSet = modelformset_factory(
    SaleItemModel,
    form=SaleItemForm,
    extra=1,
    can_delete=True
)


SaleItemEditFormSet = modelformset_factory(
    SaleItemModel,
    form=SaleItemForm,
    extra=0,
    can_delete=True
)


SaleCategoryEmptyFormSet = modelformset_factory(
    SaleCategoryEmpty,
    form=SaleCategoryEmptyForm,
    extra=0,
    can_delete=True
)

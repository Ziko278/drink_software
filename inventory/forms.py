from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Select, TextInput, CheckboxInput, CheckboxSelectMultiple, DateInput, \
    modelformset_factory, inlineformset_factory
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from inventory.models import *
from django.contrib.auth.models import Group

from sale.models import SaleModel, SaleItemModel


class CategoryForm(ModelForm):
    """   """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = CategoryModel.objects.filter(name__iexact=name)

        # Exclude current instance when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise ValidationError("Product Category with this name already exists")
        return name

    def clean_number_of_empty(self):
        """
        Validates that 'number_of_empty' is not a negative value.
        """
        number_of_empty = self.cleaned_data['number_of_empty']
        if number_of_empty < 0:
            raise ValidationError("Number of empties cannot be negative.")
        return number_of_empty

    class Meta:
        model = CategoryModel
        fields = '__all__'

        widgets = {

        }


class CategoryEditForm(ModelForm):
    """   """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = CategoryModel.objects.filter(name__iexact=name)

        # Exclude current instance when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise ValidationError("Drink Category with this name already exists")
        return name

    class Meta:
        model = CategoryModel
        exclude = ['number_of_empty']

        widgets = {

        }


class EmptyAdjustmentForm(forms.ModelForm):
    class Meta:
        model = EmptyAdjustmentModel
        fields = ['category', 'adjustment_type', 'reason', 'amount', 'comment']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'adjustment_type': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount <= 0:
            raise forms.ValidationError("Amount must be a positive integer.")
        return amount

    def clean(self):
        cleaned_data = super().clean()
        adjustment_type = cleaned_data.get('adjustment_type')
        category = cleaned_data.get('category')
        amount = cleaned_data.get('amount')

        if adjustment_type == 'subtract' and category and amount:
            if amount > category.number_of_empty:
                raise forms.ValidationError(
                    f"Cannot subtract {amount} crates. Only {category.number_of_empty} available."
                )


class ProductForm(ModelForm):
    """   """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        category = self.cleaned_data.get('category')

        if name and category:
            qs = ProductModel.objects.filter(name__iexact=name, category=category)

            # Exclude current instance when editing
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise ValidationError("A product with this name already exists in this category.")

        return name

    class Meta:
        model = ProductModel
        exclude = ['initial_quantity_left', 'initial_quantity']

        widgets = {
            'section': CheckboxSelectMultiple(attrs={

            })
        }


class ProductEditForm(ModelForm):
    """   """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_name(self):
        name = self.cleaned_data.get('name')
        category = self.cleaned_data.get('category')

        if name and category:
            qs = ProductModel.objects.filter(name__iexact=name, category=category)

            # Exclude current instance when editing
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise ValidationError("A product with this name already exists in this category.")

        return name

    class Meta:
        model = ProductModel
        exclude = ['last_cost_price', 'initial_quantity_left', 'initial_quantity']

        widgets = {
            'section': CheckboxSelectMultiple(attrs={

            })
        }


class SupplierForm(ModelForm):
    """   """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'products':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = Group.objects.filter(name__iexact=name)

        # Exclude current instance when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise ValidationError("A Supplier with this name already exists")
        return name

    class Meta:
        model = SupplierModel
        fields = '__all__'

        widgets = {

        }


class SupplierEditForm(ModelForm):
    """   """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'products':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = Group.objects.filter(name__iexact=name)

        # Exclude current instance when editing
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise ValidationError("A Supplier with this name already exists")
        return name

    class Meta:
        model = SupplierModel
        exclude = ['initial_balance', 'balance']

        widgets = {

        }


class StockInSummaryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

        if not self.instance.pk:
            self.initial['date'] = timezone.now().strftime('%Y-%m-%d')

    class Meta:
        model = StockInSummaryModel
        # ONLY include 'date' as per your StockInSummaryModel definition
        fields = ['date', 'status', 'empty', 'supplier', 'total_quantity', 'total_empty']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'date': 'Receipt Date',
        }


class StockInItemForm(forms.ModelForm):
    class Meta:
        model = StockInModel
        fields = ['product', 'quantity_added', 'unit_cost_price']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control product-select'}),
            'quantity_added': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.01', 'required': True}),
            'unit_cost_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0.00', 'required': True}),
            'unit_selling_price': forms.NumberInput(
                attrs={'class': 'form-control selling-price-input', 'step': '0.01', 'min': '0.00'}),

        }
        labels = {
            'product': 'Product',
            'quantity_added': 'Quantity Received',
            'unit_cost_price': 'Unit Cost',
        }

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        quantity_added = cleaned_data.get('quantity_added')
        unit_cost_price = cleaned_data.get('unit_cost_price')

        if not self.cleaned_data.get('DELETE', False):
            if product and (quantity_added is None or quantity_added <= 0):
                self.add_error('quantity_added', 'Quantity must be greater than zero.')
            if product and (unit_cost_price is None or unit_cost_price < 0):
                self.add_error('unit_cost_price', 'Unit cost cannot be negative.')

        return cleaned_data


StockInCreateFormSet = modelformset_factory(
    StockInModel,
    form=StockInItemForm,
    # --- ADJUSTMENT START ---
    extra=1, # This is the line to change from 1 to 0
    # --- ADJUSTMENT END ---
    can_delete=True,
    fields=['product', 'quantity_added', 'unit_cost_price', 'unit_selling_price']
)


StockInFormSet = modelformset_factory(
    StockInModel,
    form=StockInItemForm,
    # --- ADJUSTMENT START ---
    extra=0, # This is the line to change from 1 to 0
    # --- ADJUSTMENT END ---
    can_delete=True,
    fields=['product', 'quantity_added', 'unit_cost_price', 'unit_selling_price']
)


class StockOutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'stock_out_empty':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = StockOutModel
        fields = '__all__'
        widgets = {

        }



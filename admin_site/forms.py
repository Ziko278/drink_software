import re

from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Select, TextInput, CheckboxInput, CheckboxSelectMultiple, DateInput
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from admin_site.models import *
from django.contrib.auth.models import Group


class SiteInfoForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })

    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")

        if not mobile:
            raise ValidationError("Mobile number is required.")

        # Remove common separators
        mobile = mobile.replace(" ", "").replace("-", "")

        # Reject multiple '+' or '+' not at the beginning
        if mobile.count('+') > 1 or ('+' in mobile and not mobile.startswith('+')):
            raise ValidationError("Invalid mobile number: '+' sign can only appear once at the beginning.")

        # Validate characters: must be digits and optionally start with '+'
        if not re.fullmatch(r'(\+?\d+)', mobile):
            raise ValidationError("Mobile number must contain only digits, with an optional leading '+'.")

        # Format checks
        if mobile.startswith("+234"):
            if len(mobile) != 14:
                raise ValidationError("Mobile number must be 14 characters long when starting with +234.")
            if not mobile[1:].isdigit():
                raise ValidationError("Invalid characters detected after '+'. Digits only.")
        elif mobile.startswith("234"):
            if len(mobile) != 13:
                raise ValidationError("Mobile number must be 13 digits long when starting with 234.")
            mobile = "+" + mobile
        elif mobile.startswith("0"):
            if len(mobile) != 11:
                raise ValidationError("Mobile number must be 11 digits long when starting with 0.")
            mobile = "+234" + mobile[1:]
        else:
            raise ValidationError("Invalid format. Number must start with +234, 234 or 0.")

        return mobile

    class Meta:
        model = SiteInfoModel
        fields = '__all__'

        widgets = {

        }


class SiteSettingForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        boolean_data = ['allow_sale_discount']
        for field in self.fields:
            if field not in boolean_data:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = SiteSettingModel
        fields = '__all__'

        widgets = {

        }


class SiteSettingEditForm(ModelForm):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        boolean_data = ['allow_sale_discount']
        for field in self.fields:
            if field not in boolean_data:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

    class Meta:
        model = SiteSettingModel
        exclude = ['opening_balance', 'opening_cash_balance', 'balance', 'cash_balance',
                   'opening_petty_cash_balance', 'petty_cash_balance']
        widgets = {

        }

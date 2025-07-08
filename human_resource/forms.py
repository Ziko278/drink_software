import re
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, TextInput, DateInput, CheckboxInput
from human_resource.models import *


class GroupForm(ModelForm):
    """"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
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
            raise ValidationError("A role with this name already exists")
        return name

    class Meta:
        model = Group
        fields = '__all__'

        widgets = {

        }


class StaffForm(ModelForm):
    """  """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['group'].queryset = Group.objects.all().order_by('name')
        for field in self.fields:
            if field not in ['create_account', 'is_driver']:
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

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            # Exclude self when updating
            qs = StaffModel.objects.filter(email=email)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise ValidationError("A staff with this email already exists.")
        return email

    class Meta:
        model = StaffModel
        fields = '__all__'
        widgets = {

        }




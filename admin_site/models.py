from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from human_resource.models import StaffModel
from inventory.models import SupplierModel
from sale.models import CustomerModel


class SiteInfoModel(models.Model):
    name = models.CharField(max_length=250)
    short_name = models.CharField(max_length=50)
    logo = models.FileField(upload_to='images/logo', blank=True, null=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.short_name.upper()

    def save(self, *args, **kwargs):
        if not self.pk and SiteInfoModel.objects.exists():
            raise ValidationError("Site Info Already Added")
        return super().save(*args, **kwargs)


class SiteSettingModel(models.Model):
    opening_balance = models.FloatField()
    balance = models.FloatField(blank=True)
    opening_cash_balance = models.FloatField()
    cash_balance = models.FloatField(blank=True)
    opening_petty_cash_balance = models.FloatField()
    petty_cash_balance = models.FloatField(blank=True)
    allow_sale_discount = models.BooleanField(default=True)
    default_reorder_level = models.IntegerField()
    crate_target_for_bonus = models.IntegerField(blank=True, null=True)
    bonus_amount_per_crate = models.FloatField(blank=True, null=True)
    minimum_unit_profit = models.FloatField()
    price_for_empty = models.FloatField()
    recommended_unit_profit = models.FloatField()
    max_customer_debt = models.IntegerField(default=0)
    max_category_crate_debt = models.IntegerField(default=0)
    max_crate_debt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettingModel.objects.exists():
            raise ValidationError("Site Setting Already Added")

        if not self.balance and self.balance != 0:
            self.balance = self.opening_balance

        if not self.cash_balance and self.cash_balance != 0:
            self.cash_balance = self.opening_cash_balance

        if not self.petty_cash_balance and self.petty_cash_balance != 0:
            self.petty_cash_balance = self.opening_petty_cash_balance

        return super().save(*args, **kwargs)

    def total_balance(self):
        return self.balance + self.cash_balance + self.petty_cash_balance


class ActivityLogModel(models.Model):
    log = models.TextField()
    category = models.CharField(max_length=50, blank=True, null=True)
    keywords = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class DashboardModel(models.Model):
    pass

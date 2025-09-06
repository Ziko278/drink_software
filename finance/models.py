from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Sum

from admin_site.models import SiteSettingModel
from human_resource.models import StaffModel
from inventory.models import SupplierModel


class ExpenseTypeModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class ExpenseModel(models.Model):
    PAYMENT_SOURCE_CHOICES = [
        ('PETTY_CASH', 'Petty Cash'),
        ('ACCOUNT_BALANCE', 'Account Balance'),
    ]

    type = models.ForeignKey(ExpenseTypeModel, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    remark = models.TextField(null=True, blank=True)
    payment_source = models.CharField(
        max_length=20,
        choices=PAYMENT_SOURCE_CHOICES,
        default='PETTY_CASH'  # Default to old behavior
    )
    date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses_created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type.name} - ₦{self.amount}"


class StaffSalaryModel(models.Model):
    staff = models.OneToOneField(StaffModel, on_delete=models.CASCADE, related_name='salary_profile')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, validators=[MinValueValidator(0)])
    account_name = models.CharField(max_length=200, null=True, blank=True)
    account_number = models.CharField(max_length=20, null=True, blank=True)
    bank = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='salary_profiles_created')

    def __str__(self):
        return f"{self.staff} - ₦{self.salary}"

    def total_bonus_for_month(self, month_date):
        # Sum bonuses for this staff in given month
        return self.staff.bonuses.filter(
            date__year=month_date.year,
            date__month=month_date.month
        ).aggregate(total=Sum('bonus'))['total'] or 0

    def total_deduction_for_month(self, month_date):
        # Sum deductions for this staff in given month
        return self.staff.deductions.filter(
            date__year=month_date.year,
            date__month=month_date.month
        ).aggregate(total=Sum('deduction'))['total'] or 0


class StaffSalaryHistoryModel(models.Model):
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name='salary_history')
    old_salary = models.DecimalField(max_digits=10, decimal_places=2)
    new_salary = models.DecimalField(max_digits=10, decimal_places=2)
    change_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-change_date']
        verbose_name_plural = "Salary History"

    def __str__(self):
        return f"{self.staff}: ₦{self.old_salary} → ₦{self.new_salary} on {self.change_date.date()}"


class StaffBonusModel(models.Model):
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name='bonuses')
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bonuses_created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bonus for {self.staff} on {self.date}"


class StaffDeductionModel(models.Model):
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name='deductions')
    deduction = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField()
    date = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deductions_created')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Deduction for {self.staff} on {self.date}"


class StaffSalaryPaymentModel(models.Model):
    staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE, related_name='salary_payments')
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2)
    target_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    deduction = models.DecimalField(max_digits=10, decimal_places=2)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField(help_text="Use the first day of the month to represent the salary month")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='salary_payments_created')
    payment_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('staff', 'month')
        ordering = ['-month']

    def __str__(self):
        return f"{self.staff} - ₦{self.total_payment} ({self.month.strftime('%B %Y')})"

    @property
    def month_display(self):
        return self.month.strftime('%B %Y')


class StaffSalarySummaryModel(models.Model):
    total_staff = models.PositiveIntegerField()
    total_bonus = models.DecimalField(max_digits=10, decimal_places=2)
    total_deduction = models.DecimalField(max_digits=10, decimal_places=2)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_SOURCE = (('cash', 'CASH'), ('bank', 'BANK'))
    payment_source = models.CharField(max_length=10, choices=PAYMENT_SOURCE)
    month = models.DateField(help_text="Use the first day of the month for reference, e.g., 2025-06-01")
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='salary_summaries_created')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('month',)
        ordering = ['-month']

    def __str__(self):
        return f"Salary Summary for {self.month.strftime('%B %Y')}"

    @property
    def month_display(self):
        return self.month.strftime('%B %Y')


TRANSFER_TYPES = [
    ('staff_to_cash', 'Staff to Office Cash'),
    ('staff_to_bank', 'Staff to Bank'),
    ('cash_to_bank', 'Office Cash to Bank'),
    ('bank_to_cash', 'Bank to Office Cash'),
    ('bank_to_petty', 'Bank to Petty Cash'),
    ('cash_to_petty', 'Office Cash to Petty Cash'),
    ('bank_to_supplier', 'Bank to Supplier'),
    ('cash_to_supplier', 'Office Cash to Supplier'),
    ('adjustment_add', 'Bank Balance Adjustment - Add'),
    ('adjustment_subtract', 'Bank Balance Adjustment - Subtract'),
]

SOURCE_DEST = [
    ('staff', 'Staff'),
    ('cash', 'Office Cash'),
    ('bank', 'Bank'),
    ('petty', 'Petty Cash'),
    ('supplier', 'Supplier'),
]


class CashTransferModel(models.Model):
    transfer_type = models.CharField(max_length=30, choices=TRANSFER_TYPES)
    source = models.CharField(max_length=10, choices=SOURCE_DEST)
    destination = models.CharField(max_length=10, choices=SOURCE_DEST)
    staff = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(SupplierModel, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.source == self.destination and not self.transfer_type.startswith('adjustment'):
            raise ValidationError("Source and destination must be different.")

        settings = SiteSettingModel.objects.first()
        if not settings:
            raise ValidationError("Site settings not configured.")

        if self.amount <= 0:
            raise ValidationError("Amount must be greater than zero.")

        if self.transfer_type == 'cash_to_bank' and self.amount > settings.cash_balance:
            raise ValidationError("Not enough cash in office.")

        if self.transfer_type == 'bank_to_cash' and self.amount > settings.balance:
            raise ValidationError("Not enough bank balance.")

        if self.transfer_type == 'bank_to_petty' and self.amount > settings.balance:
            raise ValidationError("Not enough bank balance.")

        if self.transfer_type == 'cash_to_petty' and self.amount > settings.cash_balance:
            raise ValidationError("Not enough office cash.")

        if self.transfer_type.startswith('staff_to') and self.staff:
            if self.amount > self.staff.wallet.balance:
                raise ValidationError("Staff does not have sufficient funds.")

        if self.transfer_type in ['bank_to_supplier', 'cash_to_supplier']:
            if not self.supplier:
                raise ValidationError("Supplier must be selected for this transfer.")
            if self.transfer_type == 'bank_to_supplier' and self.amount > settings.balance:
                raise ValidationError("Not enough bank balance.")
            if self.transfer_type == 'cash_to_supplier' and self.amount > settings.cash_balance:
                raise ValidationError("Not enough cash in office.")

        if self.transfer_type.startswith('adjustment') and not self.comment:
            raise ValidationError("Adjustment must include a comment.")

        if self.transfer_type == 'adjustment_subtract' and self.amount > settings.balance:
            raise ValidationError("Adjustment subtraction exceeds bank balance.")

    def save(self, *args, **kwargs):
        self.clean()
        settings = SiteSettingModel.objects.first()

        if self.transfer_type == 'staff_to_cash':
            self.staff.wallet.balance -= self.amount
            self.staff.wallet.save()
            settings.cash_balance += self.amount

        elif self.transfer_type == 'staff_to_bank':
            self.staff.wallet.balance -= self.amount
            self.staff.wallet.save()
            settings.balance += self.amount

        elif self.transfer_type == 'cash_to_bank':
            settings.cash_balance -= self.amount
            settings.balance += self.amount

        elif self.transfer_type == 'bank_to_cash':
            settings.balance -= self.amount
            settings.cash_balance += self.amount

        elif self.transfer_type == 'bank_to_petty':
            settings.balance -= self.amount
            settings.petty_cash_balance += self.amount

        elif self.transfer_type == 'cash_to_petty':
            settings.cash_balance -= self.amount
            settings.petty_cash_balance += self.amount

        elif self.transfer_type == 'bank_to_supplier':
            settings.balance -= self.amount
            self.supplier.balance += self.amount
            self.supplier.save()

        elif self.transfer_type == 'cash_to_supplier':
            settings.cash_balance -= self.amount
            self.supplier.balance += self.amount
            self.supplier.save()

        elif self.transfer_type == 'adjustment_add':
            settings.balance += self.amount

        elif self.transfer_type == 'adjustment_subtract':
            settings.balance -= self.amount

        settings.save()
        super().save(*args, **kwargs)



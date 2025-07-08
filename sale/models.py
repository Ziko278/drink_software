from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, F  # F is useful for database-level updates
from django.utils import timezone
from django.core.validators import MinValueValidator
from human_resource.models import StaffModel
from inventory.models import ProductModel, CategoryModel, StockInModel  # Added StockInModel import as it's related


class CustomerModel(models.Model):
    full_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')],
                              default='active')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.full_name.title()


class CustomerWalletModel(models.Model):
    customer = models.OneToOneField(CustomerModel, on_delete=models.CASCADE, related_name='customer_wallet')
    # Changed to DecimalField for financial accuracy
    initial_debt = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    initial_debt_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=Decimal('0.00'))
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=Decimal('0.00'))

    def __str__(self):
        return f"Wallet for {self.customer.full_name}"


class CustomerCrateDebtModel(models.Model):
    # Changed to ForeignKey to allow multiple crate debt entries per customer (one per category)
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE,
                                 related_name='crate_debts')  # Renamed related_name to plural
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='category_crate_debts')
    # Changed to DecimalField for precise quantity tracking of crates
    crate = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    class Meta:
        # Ensures a customer has only one crate debt entry for a specific category
        unique_together = ('customer', 'category')
        verbose_name = "Customer Crate Debt"
        verbose_name_plural = "Customer Crate Debts"

    def __str__(self):
        return f"{self.customer.full_name} - {self.category.name}: {self.crate} crates owed"


# Monetary debt repayment
class CustomerDebtRepaymentModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='debt_repayments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, validators=[], default=Decimal('0.00'))
    payment_method = models.CharField(
        max_length=20,
        choices=[('cash', 'Cash'), ('bank', 'Bank'), ('driver', 'Driver')],
        default='cash'
    )
    driver = models.ForeignKey(StaffModel, null=True, blank=True, on_delete=models.SET_NULL)
    note = models.TextField(blank=True, null=True)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Debt Repayment"
        verbose_name_plural = "Debt Repayments"

    def __str__(self):
        return f"₦{self.amount_paid} repayment by {self.customer.full_name} on {self.created_at.date()}"


# Crate refund by category
class CustomerCrateReturnModel(models.Model):
    RETURN_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('empty', 'Empty'),
    ]
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name='crate_returns')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    crates_returned = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    note = models.TextField(blank=True, null=True)
    return_method = models.CharField(max_length=10, choices=RETURN_METHOD_CHOICES, default='empty')
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(
        max_length=20,
        choices=[('cash', 'Cash'), ('bank', 'Bank'), ('driver', 'Driver')],
        default='cash', blank=True, null=True
    )
    driver = models.ForeignKey(StaffModel, null=True, blank=True, on_delete=models.SET_NULL)
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('customer', 'category', 'created_at')
        ordering = ['-created_at']
        verbose_name = "Crate Return"
        verbose_name_plural = "Crate Returns"
        
    def save(self, *args, **kwargs):
        from admin_site.models import SiteSettingModel
        # Only auto-calc amount_paid on cash returns
        if self.return_method == 'cash':
            setting = SiteSettingModel.objects.first()
            price = None
            if setting and setting.price_for_empty is not None:
                # Convert float to Decimal safely
                price = Decimal(str(setting.price_for_empty))
            if price is not None:
                self.amount_paid = self.crates_returned * price
            else:
                self.amount_paid = None
        else:
            # For empty returns, ensure amount_paid is empty
            self.amount_paid = None

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.full_name} returned {self.crates_returned} crates of {self.category.name}"


class SaleModel(models.Model):
    """
    Represents a single completed transaction (e.g., a customer's purchase).
    """
    SALE_STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('pending', 'Pending'),
        ('refunded', 'Refunded'),
        ('cancelled', 'Cancelled'),
    ]
    SALE_PAYMENT_STATUS_CHOICES = [
        ('none', 'None'),        # No payment made yet
        ('partial', 'Partial'),  # Some payment made, but not full
        ('complete', 'Complete') # Full payment received
    ]
    SALE_DELIVERY_STATUS_CHOICES = [
        ('self', 'Self Collection'),
        ('driver', 'Delivered by Driver'),
    ]
    SALE_PAYMENT_DESTINATION_CHOICES = [
        ('bank', 'Paid to Bank'),
        ('cash', 'Paid Cash'),
        ('driver', 'Paid to Driver'),
    ]

    transaction_id = models.CharField(max_length=50, unique=True, blank=True)
    sale_date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       validators=[MinValueValidator(Decimal('0.00'))])
    total_amount_paid = models.DecimalField(max_digits=10, decimal_places=2,
                                            default=Decimal('0.00'))
    total_amount_left = models.DecimalField(max_digits=10, decimal_places=2,
                                            default=Decimal('0.00'), blank=True)
    total_discount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'),
                                         blank=True, help_text="Total discount across all sale items.")
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=SALE_STATUS_CHOICES)
    payment_status = models.CharField(max_length=20, choices=SALE_PAYMENT_STATUS_CHOICES,
                                      blank=True, default='none')
    payment_destination = models.CharField(max_length=20, choices=SALE_PAYMENT_DESTINATION_CHOICES,
                                           blank=True)
    delivery_status = models.CharField(max_length=20, choices=SALE_DELIVERY_STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    driver = models.ForeignKey(StaffModel, on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='deliveries')

    class Meta:
        ordering = ['-sale_date']
        verbose_name_plural = "Sales"

    def __str__(self):
        return f"Sale #{self.transaction_id or self.pk} - {self.sale_date.strftime('%Y-%m-%d %H:%M')}"

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = f"SALE-{timezone.now().strftime('%Y%m%d%H%M%S%f')[:-3]}"
        if self.total_amount_paid == Decimal('0.00'):
            self.payment_status = 'none'
        elif self.total_amount_paid >= self.total_amount:
            self.payment_status = 'complete'
        else:
            self.payment_status = 'partial'

        self.total_amount_left = self.total_amount - self.total_amount_paid
        super().save(*args, **kwargs)

    @property
    def total_items_count(self):
        return self.items.aggregate(
            total_qty=Sum('quantity', output_field=models.DecimalField())
        )['total_qty'] or Decimal('0.00')

    @property
    def total_profit(self):
        return self.items.aggregate(
            total_pft=Sum('profit', output_field=models.DecimalField())
        )['total_pft'] or Decimal('0.00')

    @property
    def total_crates_brought(self):
        return self.category_empties.aggregate(
            total=Sum('empty_brought')
        )['total'] or Decimal('0.00')

    @property
    def total_crate_debt(self):
        return self.category_empties.aggregate(
            total=Sum('empty_owed')
        )['total'] or Decimal('0.00')


class SaleItemModel(models.Model):
    """
    Represents a single product line item within a Sale.
    """
    sale = models.ForeignKey(SaleModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    stock = models.ForeignKey('inventory.StockInModel', on_delete=models.SET_NULL, null=True, blank=True)

    unit_discount = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=Decimal('0.00'), blank=True
    )
    total_discount = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=Decimal('0.00'), blank=True
    )

    quantity = models.DecimalField(max_digits=10, decimal_places=2,
                                   validators=[MinValueValidator(Decimal('0.01'))])
    unit_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     validators=[MinValueValidator(Decimal('0.01'))])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,
                                   validators=[MinValueValidator(Decimal('0.00'))])
    cost_price = models.DecimalField(max_digits=10, decimal_places=2,
                                     validators=[MinValueValidator(Decimal('0.00'))])
    profit = models.DecimalField(max_digits=10, decimal_places=2,
                                 validators=[MinValueValidator(Decimal('0.00'))])

    class Meta:
        unique_together = ('sale', 'product')
        verbose_name = "Sale Item"
        verbose_name_plural = "Sale Items"

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Sale #{self.sale.transaction_id or self.sale.pk}"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        self.profit = (self.unit_price - self.cost_price) * self.quantity
        super().save(*args, **kwargs)


class SaleCategoryEmpty(models.Model):
    """
    Represents crate tracking for a product category in a single sale.
    """
    sale = models.ForeignKey(SaleModel, on_delete=models.CASCADE, related_name='category_empties')
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)

    empty_expected = models.DecimalField(max_digits=10, decimal_places=2,
                                         validators=[MinValueValidator(Decimal('0.00'))])
    empty_brought = models.DecimalField(max_digits=10, decimal_places=2,
                                        validators=[MinValueValidator(Decimal('0.00'))])
    empty_owed = models.DecimalField(max_digits=10, decimal_places=2,
                                     validators=[MinValueValidator(Decimal('0.00'))])

    class Meta:
        unique_together = ('sale', 'category')
        verbose_name = "Sale Category Crate Record"
        verbose_name_plural = "Sale Category Crate Records"

    def __str__(self):
        return f"{self.category.name}: Expected {self.empty_expected}, Brought {self.empty_brought}, Owed {self.empty_owed}"


class ReturnModel(models.Model):
    """
    Records product returns linked to a specific SaleItemModel for accurate pricing.
    """
    RETURN_REASON_CHOICES = [
        ('damaged', 'Damaged Product'),
        ('wrong_item', 'Wrong Item Shipped/Purchased'),
        ('customer_changed_mind', 'Customer Changed Mind'),
        ('defective', 'Defective Product'),
        ('other', 'Other'),
    ]

    # CRITICAL CHANGE: Linked to SaleItemModel for accurate historical pricing
    sale_item = models.ForeignKey(SaleItemModel, on_delete=models.CASCADE, related_name='returns_for_item')
    # Removed direct 'product' ForeignKey as it's accessible via sale_item.product

    # Changed to DecimalField for precise quantity tracking
    quantity_returned = models.DecimalField(max_digits=10, decimal_places=2,
                                            validators=[MinValueValidator(Decimal('0.01'))])

    return_date = models.DateTimeField(default=timezone.now)
    reason = models.CharField(max_length=50, choices=RETURN_REASON_CHOICES, default='customer_changed_mind')

    # Changed to DecimalField for financial accuracy
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                        validators=[MinValueValidator(Decimal('0.00'))])

    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Returns"
        ordering = ['-return_date']
        # Optional: Add unique_together if a single sale item can only be returned once
        # or a return is strictly one-to-one with a sale item (e.g., ('sale_item', 'return_date'))

    def __str__(self):
        return f"Return for Sale #{self.sale_item.sale.transaction_id or self.sale_item.sale.pk} - {self.sale_item.product.name} ({self.quantity_returned})"

    def save(self, *args, **kwargs):
        # Calculate refund_amount based on the original unit_price from SaleItemModel
        if not self.refund_amount and self.sale_item:  # Check if sale_item exists
            self.refund_amount = self.sale_item.unit_price * self.quantity_returned
        super().save(*args, **kwargs)
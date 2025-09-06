from decimal import Decimal

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum, F
from django.utils import timezone
from django.core.validators import MinValueValidator


class CategoryModel(models.Model):
    """
    Represents a category for products (e.g. 'Beverages').
    """
    name = models.CharField(max_length=100, unique=True)
    number_of_empty = models.FloatField()
    price_for_empty = models.FloatField(default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name.upper()


class EmptyAdjustmentModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    adjustment_type = models.CharField(max_length=10, choices=[
        ('add', 'Add to Empties'),
        ('subtract', 'Remove from Empties'),
    ])
    reason = models.CharField(max_length=20, choices=[
        ('purchase', 'New Purchase'),
        ('theft', 'Theft'),
        ('correction', 'Correction'),
	('damage', 'Damage'),
        ('other', 'Other'),
    ])
    amount = models.IntegerField()
    comment = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Amount must be a positive whole number.")

        if self.adjustment_type == 'subtract' and self.amount > self.category.number_of_empty:
            raise ValidationError("Cannot subtract more than the current number of empties.")

    def save(self, *args, **kwargs):
        self.clean()

        if self.adjustment_type == 'add':
            self.category.number_of_empty += self.amount
        elif self.adjustment_type == 'subtract':
            self.category.number_of_empty -= self.amount

        self.category.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name}: {'+' if self.adjustment_type == 'add' else '-'}{self.amount} crates"


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    TYPE = (('bottle', 'BOTTLE'), ('can', 'CAN'))
    type = models.CharField(max_length=10, choices=TYPE, default='bottle')
    name = models.CharField(max_length=255)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    last_cost_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.0, validators=[MinValueValidator(0.01)])
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True)
    initial_quantity = models.IntegerField(validators=[MinValueValidator(0)], blank=True)
    initial_quantity_left = models.IntegerField(validators=[MinValueValidator(0)], blank=True)
    reorder_level = models.IntegerField(default=10, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    def save(self, *args, **kwargs):
        if not self.id:
            self.initial_quantity = self.quantity
            self.initial_quantity_left = self.quantity

        return super().save(*args, **kwargs)


class SupplierModel(models.Model):
    """
    Represents a supplier of products.
    """
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    initial_balance = models.FloatField(blank=True, default=0.0)
    balance = models.FloatField(default=0.0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.balance = self.initial_balance

        return super().save(*args, **kwargs)


class SupplierCashFlowHistoryModel(models.Model):
    """

    """
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    initial_amount = models.FloatField()
    amount = models.FloatField()
    final_amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Supplier Balance History"


class PriceHistoryModel(models.Model):
    """
    Keeps a historical record of product price changes.
    Useful for reporting and understanding pricing strategies.
    """
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='price_history')
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    change_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-change_date']
        verbose_name_plural = "Price History"

    def __str__(self):
        return f"{self.product.name}: {self.old_price} -> {self.new_price} on {self.change_date.date()}"


class StockInModel(models.Model):
    """
    Records a single instance of stock being added for a product.
    'is_tampered' logic is now handled by StockInSummaryModel.
    """
    product = models.ForeignKey('ProductModel', on_delete=models.CASCADE, related_name='stock_ins')

    quantity_added = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    # IMPORTANT: Use Decimal('0.00') as default for DecimalField to avoid type mismatches
    quantity_left = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal('0.00'))
    quantity_sold = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal('0.00'))
    quantity_stocked_out = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=Decimal('0.00'))
    unit_cost_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    unit_selling_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])

    date_added = models.DateField(blank=True, default=timezone.now)
    status = models.CharField(max_length=10, default='active', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('human_resource.StaffModel', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Stock In Record"
        verbose_name_plural = "Stock In Records"
        ordering = ['-date_added', '-created_at']

    def __str__(self):
        # Added safety checks for properties to prevent AttributeError if product is not loaded
        product_name = self.product.name if hasattr(self, 'product') and self.product else "Unknown Product"
        return f"Added {self.quantity_added} of {product_name} @ {self.unit_cost_price}"

    @property
    def total_cost_price(self):
        """Calculates the total cost for this specific stock-in entry, with safety checks."""
        # Added safety checks for None values before multiplication
        if self.quantity_added is None or self.unit_cost_price is None:
            return Decimal('0.00')
        return self.quantity_added * self.unit_cost_price

    def save(self, *args, **kwargs):
        if not self.pk:
            self.quantity_left = self.quantity_added

        if self.quantity_left <= Decimal('0.00'):
            self.status = 'finished'
        else:
            self.status = 'active'

        super(StockInModel, self).save(*args, **kwargs)


class StockInSummaryModel(models.Model):
    """
    Represents a summary or header for a collection of StockInModel records.
    """
    STATUS = (('pending', 'PENDING'), ('confirmed', 'CONFIRMED'))
    products = models.ManyToManyField(StockInModel, blank=True,
                                      help_text="Individual stock-in records included in this summary.")

    date = models.DateField(default=timezone.now, help_text="The overall date of this stock-in summary.")

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        help_text="Status of the stock-in. 'Pending' means not yet committed to inventory. 'Confirmed' means committed."
    )
    supplier = models.ForeignKey(SupplierModel, on_delete=models.SET_NULL, null=True)
    total_quantity = models.IntegerField(default=0)
    empty = models.IntegerField(default=0)
    total_empty = models.IntegerField(default=0)
    is_tampered = models.BooleanField(
        default=False,
        help_text="Indicates if any stock from this summary has been affected by a sale or stock-out. Tampered summaries cannot be edited/deleted."
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when this summary record was created.")
    created_by = models.ForeignKey('human_resource.StaffModel', on_delete=models.SET_NULL, null=True, blank=True,
                                   help_text="Staff member who created this summary.")

    class Meta:
        verbose_name = "Stock In Summary"
        verbose_name_plural = "Stock In Summaries"
        ordering = ['-date', '-created_at']
        # You will need to define this custom permission here for the views to work:
        # permissions = [("process_stockinsummarymodel", "Can process pending stock-in summaries")]

    def __str__(self):
        # Added safety check for products.all() which might cause issues before objects are loaded
        # Also, using the summary's PK in __str__ is often more stable before M2M relationships are fully established.
        return f"Summary {self.pk} ({self.status.title()})"

    @property
    def total_summary_cost(self):
        """
        Calculates the total cost for all products linked to this summary.
        Uses Django's aggregation for efficiency on ManyToMany.
        """
        if not self.pk:  # For unsaved instances, return 0
            return Decimal('0.00')
        cost_sum = self.products.aggregate(
            total=Sum(F('quantity_added') * F('unit_cost_price'), output_field=models.DecimalField())
        )['total']
        return cost_sum or Decimal('0.00')

    @property
    def total_quantity_added(self):
        """
        Calculates the sum of 'quantity_added' for all StockInModel instances
        (products) linked to this summary. E.g., 10 Coke + 15 Pepsi = 25.
        """
        if not self.pk:  # For unsaved instances, return 0
            return Decimal('0.00')

        # Aggregate the sum of the 'quantity_added' field from all related StockInModel instances
        quantity_sum = self.products.aggregate(
            total=Sum('quantity_added', output_field=models.DecimalField())
        )['total']

        # Return the sum, defaulting to Decimal('0.00') if no products are linked or sum is None
        return quantity_sum or Decimal('0.00')


class StockOutModel(models.Model):
    """
    Records stock removal for reasons other than sales (e.g., damage, internal use, write-off).
    """
    stock = models.ForeignKey(StockInModel, on_delete=models.CASCADE, related_name='stock_outs')
    quantity_removed = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], help_text="Quantity of product removed.")
    cost_of_removed_stock = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Calculated cost of the stock removed based on costing method.")
    reason = models.TextField(help_text="Why was this stock removed (e.g., 'Damaged', 'Internal Use', 'Lost').")
    date_removed = models.DateField(default=timezone.now, blank=True, help_text="The date this stock was physically removed.")
    stock_out_empty = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when this record was created.")
    created_by = models.ForeignKey('human_resource.StaffModel', on_delete=models.SET_NULL, null=True, blank=True, help_text="Staff member who recorded this stock out.")

    class Meta:
        verbose_name = "Stock Out Record"
        verbose_name_plural = "Stock Out Records"
        ordering = ['-date_removed', '-created_at']

    def __str__(self):
        # Safely access product name from related StockInModel
        product_name = self.stock.product.name if self.stock and hasattr(self.stock, 'product') and self.stock.product else "Unknown Product"
        return f"Removed {self.quantity_removed} of {product_name} - Reason: {self.reason[:50]}"

    def save(self, *args, **kwargs):
        """
        Automatically calculates the 'cost_of_removed_stock' before saving.
        Updates 'quantity_left' on the associated StockInModel.
        Crucially, it marks the parent StockInSummaryModel as 'is_tampered'.
        """
        if self.stock and self.quantity_removed is not None:
            # Calculate cost_of_removed_stock
            if self.stock.unit_cost_price is not None:
                self.cost_of_removed_stock = self.quantity_removed * self.stock.unit_cost_price
            else:
                self.cost_of_removed_stock = Decimal('0.00')

            # Update quantity_left on the associated StockInModel
            if self.stock.quantity_left >= self.quantity_removed:
                self.stock.quantity_left -= self.quantity_removed
                self.stock.save(update_fields=['quantity_left', 'status']) # Update status in case it becomes 'finished'
            else:
                # If trying to remove more than left in this batch, zero out and proceed
                self.stock.quantity_left = Decimal('0.00')
                self.stock.save(update_fields=['quantity_left', 'status'])

            # CRITICAL: Mark the parent StockInSummaryModel as tampered
            # A StockInModel can be part of multiple StockInSummaryModels via ManyToMany.
            # We need to mark ALL relevant parent summaries as tampered.
            parent_summaries = self.stock.stockinsummarymodel_set.all()
            for summary in parent_summaries:
                if not summary.is_tampered: # Only update if not already tampered
                    summary.is_tampered = True
                    summary.save(update_fields=['is_tampered'])
        else:
            self.cost_of_removed_stock = Decimal('0.00')

        super().save(*args, **kwargs)

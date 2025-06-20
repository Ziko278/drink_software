from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.html import escape
from django.urls import reverse
from django.utils.timezone import now

from admin_site.models import ActivityLogModel
from inventory.models import EmptyAdjustmentModel, PriceHistoryModel, ProductModel, StockInSummaryModel, SupplierModel, \
    StockInModel


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.html import escape
from django.utils.timezone import now


@receiver(post_save, sender=ProductModel)
def product_initial_stock(sender, instance, created, **kwargs):
    """
    Records initial stock in StockInModel when a new ProductModel instance is created
    with quantity > 0. Also logs the action.
    """
    if created and instance.quantity > 0:
        try:
            product = instance
            user = getattr(instance, 'updated_by', None)
            staff = getattr(user, 'profile', None)
            staff = getattr(staff, 'staff', None) if staff else None

            # Create a StockIn record
            StockInModel.objects.create(
                product=product,
                quantity_added=product.quantity,
                quantity_left=product.quantity,
                unit_cost_price=product.last_cost_price,
                unit_selling_price=product.selling_price,
                created_by=staff
            )

            # Prepare activity log
            staff_html = (
                f"<a href='{reverse('staff_detail', kwargs={'pk': staff.id})}'><b>{staff.full_name}</b></a>"
                if staff else "Unknown Staff"
            )

            product_link = reverse('product_detail', kwargs={'pk': instance.pk})

            log_html = f"""
                <div style='border-radius:5px' class='text-white bg-primary p-2'>
                    <p>{staff_html} added a new Product: {product.name.upper()} <br>
                    Qty: {product.quantity}, Cost Price: ₦{product.last_cost_price:,.2f}, Selling Price: ₦{product.selling_price:,.2f}.
                    <br>
                    <a href="{product_link}"><b>{escape(instance.name)}</b></a>
                    <br><span style='float:right'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
                </div>
            """

            ActivityLogModel.objects.create(
                log=log_html,
                user=user,
                category='inventory',
                keywords='inventory__initial_stock'
            )

        except Exception as e:
            print(f"Error recording initial stock for {instance.name}: {e}")


@receiver(pre_save, sender=ProductModel)
def record_price_change(sender, instance, **kwargs):
    """
    Records a price change in PriceHistoryModel when a ProductModel instance is saved
    and its price field has been modified.
    """
    if instance.pk: # Check if the instance already exists (i.e., it's an update, not a creation)
        try:
            # Get the old instance from the database
            old_instance = sender.objects.get(pk=instance.pk)
            # Compare the old price with the new price
            if old_instance.selling_price != instance.selling_price:
                # If prices are different, create a PriceHistoryModel object
                PriceHistoryModel.objects.create(
                    product=instance,
                    old_price=old_instance.selling_price,
                    new_price=instance.selling_price
                )

                # Prepare activity log
                user = getattr(instance, 'updated_by', None)
                staff = getattr(user, 'profile', None)
                staff = getattr(staff, 'staff', None) if staff else None

                staff_html = (
                    f"<a href='{reverse('staff_detail', kwargs={'pk': staff.id})}'><b>{staff.full_name}</b></a>"
                    if staff else "Unknown Staff"
                )

                product_link = reverse('product_detail', kwargs={'pk': instance.pk})

                log_html = f"""
                                <div style='border-radius:5px' class='text-white bg-primary p-2'>
                                    <p>{staff_html} updated the price of
                                    <a href="{product_link}"><b>{escape(instance.name)}</b></a>
                                    from ₦{old_instance.selling_price:,.2f} to ₦{instance.selling_price:,.2f}.
                                    <br><span style='float:right'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
                                </div>
                                """

                ActivityLogModel.objects.create(log=log_html, user=user, category='inventory')

        except sender.DoesNotExist:
            # This can happen if the object is new but has a PK assigned before save
            # Or if there's a race condition. For simplicity, we'll ignore for now.
            pass
        except Exception as e:
            # Log any other exceptions that might occur
            print(f"Error recording price change for {instance.name}: {e}")


@receiver(post_save, sender=EmptyAdjustmentModel)
def log_category_empty_adjustment(sender, instance, created, **kwargs):
    if not created:
        return

    user = instance.created_by
    executor_staff = getattr(user, 'profile', None)
    executor_staff = getattr(executor_staff, 'staff', None) if executor_staff else None

    executor_html = (
        f"<a href='{reverse('staff_detail', kwargs={'pk': executor_staff.id})}'>"
        f"<b>{executor_staff.full_name}</b></a>" if executor_staff else "N/A"
    )

    # Format adjustment type display nicely
    adj_type_display = 'Added' if instance.adjustment_type == 'add' else 'Removed'

    log_html = f"""
    <div style='border-radius:5px' class='text-white bg-primary p-2'>
        <p>{executor_html} {adj_type_display} <b>{instance.amount}</b> crate(s) for category 
        <b>{escape(instance.category.name)}</b>.<br>
        Reason: {escape(instance.reason.replace('_', ' ').capitalize())}<br>
        Note: {escape(instance.comment or 'No comment')}
        <br><span style='float:right'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
    </div>
    """

    ActivityLogModel.objects.create(log=log_html, user=user, category='inventory')


@receiver(post_save, sender=SupplierModel)
def log_supplier_creation(sender, instance, created, **kwargs):
    if not created:
        return

    user = instance.updated_by
    executor_staff = getattr(user, 'profile', None)
    executor_staff = getattr(executor_staff, 'staff', None) if executor_staff else None

    executor_html = (
        f"<a href='{reverse('staff_detail', kwargs={'pk': executor_staff.id})}'>"
        f"<b>{escape(executor_staff.full_name)}</b></a>" if executor_staff else "N/A"
    )

    log_html = f"""
    <div style='border-radius:5px' class='text-white bg-primary p-2'>
        <p>{executor_html} created a new supplier: <b>{escape(instance.name)}</b> under category 
        <b>{escape(instance.category.name.upper())}</b> with an opening balance of 
        <b>₦{instance.initial_balance}</b>.<br>
        <span style='float:right'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
    </div>
    """

    ActivityLogModel.objects.create(log=log_html, user=user, category='inventory', supplier=instance)

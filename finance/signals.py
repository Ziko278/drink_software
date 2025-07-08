from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.timezone import now
from admin_site.models import ActivityLogModel
from finance.models import StaffSalaryModel, StaffSalaryHistoryModel, CashTransferModel
from django.utils.html import escape


@receiver(pre_save, sender=StaffSalaryModel)
def track_salary_change(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_instance = StaffSalaryModel.objects.get(pk=instance.pk)
            old_salary = old_instance.salary
            new_salary = instance.salary

            if old_salary != new_salary:
                StaffSalaryHistoryModel.objects.create(
                    staff=instance.staff,
                    old_salary=old_salary,
                    new_salary=new_salary
                )
        except StaffSalaryModel.DoesNotExist:
            pass


@receiver(post_save, sender=CashTransferModel)
def log_cash_transfer(sender, instance, created, **kwargs):
    if not created:
        return

    user = instance.created_by
    executor_staff = getattr(getattr(user, 'profile', None), 'staff', None)

    executor_html = (
        f"<a href='{reverse('staff_detail', kwargs={'pk': executor_staff.id})}'><b>{executor_staff.full_name}</b></a>"
        if executor_staff else "N/A"
    )

    is_adjustment = instance.transfer_type.startswith('adjustment_')

    # Destination staff
    destination_staff_html = ''
    if instance.destination == 'staff' and instance.destination_staff:
        destination_staff_html = f"Destination Staff: <a href='{reverse('staff_detail', kwargs={'pk': instance.destination_staff.id})}'><b>{instance.destination_staff.full_name}</b></a><br>"

    # Supplier
    supplier_html = ''
    if instance.destination == 'supplier' and instance.supplier:
        supplier_html = f"Supplier: <b>{escape(instance.supplier.name)}</b><br>"

    # From/To display
    from_to_line = ''
    if not is_adjustment:
        source_label = instance.get_source_display()
        dest_label = instance.get_destination_display()
        from_to_line = f"From <b>{source_label}</b> to <b>{dest_label}</b><br>"

    # Format log entry
    log_html = f"""
    <div style='border-radius:5px' class='text-white bg-dark p-2'>
        <p>{executor_html} executed cash transfer: <b>{instance.get_transfer_type_display()}</b> of ₦{instance.amount:,.2f}.<br>
        {from_to_line}
        {destination_staff_html}{supplier_html}
        Note: {escape(instance.comment or 'No comment')}
        <br><span style='float:right'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span></p>
    </div>
    """

    ActivityLogModel.objects.create(
        log=log_html,
        user=user,
        category='finance',
        keywords=f'finance__cash_transfer__{instance.transfer_type}'
    )

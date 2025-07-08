from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.html import escape
from django.urls import reverse
from django.utils.timezone import now
from .models import SiteSettingModel, ActivityLogModel


@receiver(pre_save, sender=SiteSettingModel)
def log_site_setting_changes(sender, instance, **kwargs):
    if not instance.pk:
        return  # Don't log on create

    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    changes = []

    for field in instance._meta.fields:
        field_name = field.name
        if field_name in ['id', 'created_at', 'updated_at', 'opening_balance', 'balance', 'opening_cash_balance',
                          'cash_balance', 'opening_petty_cash_balance', 'petty_cash_balance']:
            continue  # skip non-user fields

        old_value = getattr(old_instance, field_name)
        new_value = getattr(instance, field_name)

        if old_value != new_value:
            changes.append(
                f"<li><b>{field.verbose_name.title()}</b> changed from <i>{escape(old_value)}</i> to <i>{escape(new_value)}</i></li>"
            )

    if not changes:
        return  # No actual changes

    # Get user from instance
    user = getattr(instance, '_changed_by', None)

    # Try to get staff name via profile -> staff
    if user:
        try:
            staff = user.profile.staff
            staff_name = staff.full_name.title()
            staff_url = reverse('staff_detail', kwargs={'pk': staff.id})
            staff_html = f"<a href='{staff_url}'><b>{escape(staff_name)}</b></a>"
        except Exception:
            staff_name = user.get_full_name() or user.username
            staff_html = f"<b>{escape(staff_name)}</b>"
    else:
        staff_html = "<b>System</b>"

    log_html = f"""
    <div class='text-white bg-danger' style='padding:5px;border-radius:5px'>
        <p>
            {staff_html} updated site settings:
            <ul>
                {''.join(changes)}
            </ul>
            <br><span style='float:right'>{now().strftime('%Y-%m-%d %H:%M:%S')}</span>
        </p>
    </div>
    """

    ActivityLogModel.objects.create(log=log_html, user=user, category='setting')

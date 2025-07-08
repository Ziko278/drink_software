# admin_site/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from finance.models import StaffSalaryModel
from human_resource.models import StaffModel, StaffProfileModel, StaffWalletModel
from django.utils.text import slugify
import random
import secrets
import string

def generate_8_char_password():
    characters = string.ascii_letters + string.digits  # Includes a-z, A-Z, 0-9
    return ''.join(secrets.choice(characters) for _ in range(8))


@receiver(post_save, sender=StaffModel)
def create_user_for_staff(sender, instance, created, **kwargs):
    if created and instance.create_account:
        if not StaffProfileModel.objects.filter(staff=instance).exists():
            # Generate username

            username = instance.email if instance.email else f"stf-{random.randrange(1000, 10000)}"
            while User.objects.filter(username=username).exists():
                username = instance.email if instance.email else f"stf-{random.randrange(1000, 10000)}"

            # Create user
            default_password = generate_8_char_password()
            user = User.objects.create_user(username=username)
            user.set_password(default_password)
            user.save()

            # Create profile
            StaffProfileModel.objects.create(user=user, staff=instance, default_password=default_password)

            # Add user to group if defined
            if instance.group:
                instance.group.user_set.add(user)

    if created:
        if not StaffWalletModel.objects.filter(staff=instance).exists():
            StaffWalletModel.objects.create(staff=instance)
        if not StaffSalaryModel.objects.filter(staff=instance).exists():
            StaffSalaryModel.objects.create(staff=instance)


@receiver(post_save, sender=StaffModel)  # Signal now listens to StaffModel
def sync_user_active_status(sender, instance, created, **kwargs):
    """
    Signal receiver to synchronize the User's is_active status
    with the StaffModel's status whenever a StaffModel
    is saved. This is done by checking the linked StaffProfileModel.
    """
    # Ensure the StaffModel instance has an associated StaffProfileModel,
    # which in turn has an associated User.
    # The 'profile' related_name on StaffProfileModel links back to StaffModel.
    if hasattr(instance, 'profile') and instance.profile.user:
        user = instance.profile.user  # Access the User through the StaffProfileModel

        # Determine the intended active status from the StaffModel's 'status' field.
        # The 'status' field is a CharField with 'active'/'inactive' choices.
        intended_user_active_status = (instance.status == 'active')

        # Check if the User's is_active status is different from the intended status.
        # This prevents unnecessary database writes if the status hasn't actually changed.
        if user.is_active != intended_user_active_status:
            user.is_active = intended_user_active_status
            # Save the User instance, explicitly updating only the 'is_active' field.
            # This is more efficient and helps prevent potential recursion issues
            # if User had its own post_save signals that might react to all field changes.
            user.save(update_fields=['is_active'])


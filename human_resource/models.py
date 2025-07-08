from django.db import models
from django.contrib.auth.models import User, Group


class StaffModel(models.Model):
    """"""
    full_name = models.CharField(max_length=50)
    image = models.FileField(upload_to='images/staff', blank=True, null=True)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=30, blank=True, choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')],
                              default='active')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    create_account = models.BooleanField(default=False, blank=True)
    is_driver = models.BooleanField(default=False, blank=True)
    crate_target_for_bonus = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.full_name.title()

    def save(self, *args, **kwargs):
        try:
            user_profile = StaffProfileModel.objects.get(staff__email=self.email)
            user = user_profile.user
            if self.email:
                user.email = self.email
            user.save()
            if self.group:
                self.group.user_set.add(user)
        except Exception:
            pass

        super(StaffModel, self).save(*args, **kwargs)


class StaffProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    staff = models.OneToOneField(StaffModel, on_delete=models.CASCADE, null=True, blank=True,
                                 related_name='staff_profile')
    default_password = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class StaffWalletModel(models.Model):
    staff = models.OneToOneField(StaffModel, on_delete=models.CASCADE, related_name='wallet')
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return self.staff.__str__()

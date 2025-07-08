from django.contrib import admin
from admin_site.models import SiteSettingModel, SiteInfoModel


admin.site.register(SiteSettingModel)
admin.site.register(SiteInfoModel)
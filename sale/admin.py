from django.contrib import admin
from sale.models import SaleModel, SaleItemModel


admin.site.register(SaleModel)
admin.site.register(SaleItemModel)
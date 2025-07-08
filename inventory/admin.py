from django.contrib import admin
from inventory.models import PriceHistoryModel, ProductModel, StockInModel


admin.site.register(PriceHistoryModel)
admin.site.register(ProductModel)
admin.site.register(StockInModel)

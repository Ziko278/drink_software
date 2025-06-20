from django.db.models import F
from admin_site.models import SiteInfoModel
from inventory.models import ProductModel


def site_info(request):
    site_info = SiteInfoModel.objects.first()
    low_stock = ProductModel.objects.filter(quantity__lte=F('reorder_level')).order_by('name')
    return {
        'site_info': site_info,
        'low_stock_list': low_stock,
        'low_stock': low_stock.count()
    }

from django.urls import path
from admin_site.views import *

urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),
    
    path('sign-in', sign_in_view, name='login'),
    path('sign-out', sign_out_view, name='logout'),
    path('change-password', user_change_password_view, name='change_password'),
    path('activity-log', ActivityLogView.as_view(), name='activity_log'),
    path('statistic/performing-customers', performing_customers_view, name='performing_customers'),
    path('statistic/performing-drivers', performing_drivers_view, name='performing_drivers'),
    path('statistic/performing-products', performing_products_view, name='performing_products'),
    path('statistic/product-sale', product_sale_view, name='product_sale_statistic'),
    path('statistic/dashboard', statistic_dashboard_view, name='statistic_dashboard'),
    path('overview/dashboard', OverviewDashboardView.as_view(), name='overview_dashboard'),

    path('site-info/<int:pk>', SiteInfoDetailView.as_view(), name='site_info_detail'),
    path('site-info/create', SiteInfoCreateView.as_view(), name='site_info_create'),
    path('site-info/<int:pk>/update', SiteInfoUpdateView.as_view(), name='site_info_edit'),

    path('site-setting/<int:pk>', SiteSettingDetailView.as_view(), name='site_setting_detail'),
    path('site-setting/create', SiteSettingCreateView.as_view(), name='site_setting_create'),
    path('site-setting/<int:pk>/update', SiteSettingUpdateView.as_view(), name='site_setting_edit'),

    
]

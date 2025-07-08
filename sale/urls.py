from django.urls import path
from sale.views import *

urlpatterns = [
    path('customer/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/index', CustomerListView.as_view(), name='customer_index'),
    path('customer/<int:pk>/detail', CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/<int:pk>/edit', CustomerUpdateView.as_view(), name='customer_edit'),
    path('customer/<int:pk>/delete', CustomerDeleteView.as_view(), name='customer_delete'),
    path('api/customers/search/', api_customer_search, name='api_customer_search'),
    path('customer/<int:customer_id>/repayment/', customer_debt_repayment_view, name='customer_debt_repayment'),
    path('customer/<int:customer_id>/crate-return/', customer_crate_return_view, name='customer_crate_return'),
    
    path('create/', sale_create_view, name='sale_create'),
    path('sales/', SaleListView.as_view(), name='sale_list'),
    path('<int:pk>/', SaleDetailView.as_view(), name='sale_detail'),
]

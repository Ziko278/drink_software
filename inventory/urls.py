from django.urls import path
from inventory.views import *

urlpatterns = [


    path('category/create', CategoryCreateView.as_view(), name='inventory_category_create'),
    path('category/index', CategoryListView.as_view(), name='inventory_category_index'),
    path('category/<int:pk>/edit', CategoryUpdateView.as_view(), name='inventory_category_edit'),
    path('category/<int:pk>/delete', CategoryDeleteView.as_view(), name='inventory_category_delete'),
    path('category/adjustments/', AddEmptyAdjustmentView.as_view(), name='add_empty_adjustment'),

    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/index', ProductListView.as_view(), name='product_index'),
    path('product/<int:pk>/detail', ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product_edit'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
    path('api/products/search/', api_product_search, name='api_product_search'),

    path('stock-in/select-category/', product_pre_stock_in_create_view, name='product_pre_stock_in'),
    path('stock-in/create/', product_stock_in_create_view, name='product_stock_in'),
    path('stock-in/list/', StockInListView.as_view(), name='stock_in_list'),
    path('stock-in/pending/', PendingStockInListView.as_view(), name='pending_stock_in_list'),
    path('stock-in/<int:pk>/detail/', product_stock_in_detail_view, name='product_stock_in_detail'),
    path('stock-in/<int:pk>/confirm/', process_pending_stock_in_view, name='process_pending_stock_in'),

    # NEW: URL for updating a stock-in summary
    path('stock-in/update/<int:pk>/', StockInSummaryUpdateView.as_view(), name='product_stock_in_update'),
    # NEW: URL for deleting a stock-in summary
    path('stock-in/delete/<int:pk>/', StockInSummaryDeleteView.as_view(), name='product_stock_in_delete'),

    # Stock Out - Creation & Listing
    path('stock-out/create/', StockOutCreateView.as_view(), name='stock_out_create'),
    path('stock-out/list/', StockOutIndexView.as_view(), name='stock_out_list'),
    
    path('supplier/create', SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/index', SupplierListView.as_view(), name='supplier_index'),
    path('supplier/<int:pk>/detail', SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/edit', SupplierUpdateView.as_view(), name='supplier_edit'),
    path('supplier/<int:pk>/delete', SupplierDeleteView.as_view(), name='supplier_delete'),
]

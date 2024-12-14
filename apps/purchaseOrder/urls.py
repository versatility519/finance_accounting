from django.urls import path
from .views import (
    PurchaseDocumentListCreateView, PurchaseDocumentDetailView,
    PurchaseOrderListCreateView, PurchaseOrderDetailView,
    PurchaseOrderItemListCreateView, PurchaseOrderItemDetailView
)

urlpatterns= [
    path('purchase_docs', PurchaseDocumentListCreateView.as_view(), name='purchase_docs-list-create'),
    path('purchase_docs/<int:pk>', PurchaseDocumentDetailView.as_view(), name='purchase_docs-detail'),
    
    path('purchase_orders', PurchaseOrderListCreateView.as_view(), name='purchase_orders-list-create'),
    path('purchase_orders/<int:pk>', PurchaseOrderDetailView.as_view(), name='purchase_orders-detail'),
   
    path('purchase_order_items', PurchaseOrderItemListCreateView.as_view(), name='purchase_order_items-list-create'),
    path('purchase_order_items/<int:pk>', PurchaseOrderItemDetailView.as_view(), name='purchase_order_items-detail'),
]
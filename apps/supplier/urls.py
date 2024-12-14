from django.urls import path
from .views import (
    CarrierListCreateView, 
    CarrierDetailView,
    
    SupplierListCreateView, 
    SupplierDetailView,
    
    SupplierItemListCreateView,
    SupplierItemDetailView,
    
    SupplierContactListCreateView,
    SupplierContactDetailView,
    
    ShippingItemCreateView,
    ShippingItemDetailView,
    
    ShipDocsListCreateView,
    ShipDocsDetailView,
    
    ShippingListCreateView,
    ShippingDetailView,
    
    SupplierPOListCreateView,
    SupplierPODetailView,
)
urlpatterns = [
    path('supplier-carriers', CarrierListCreateView.as_view(), name='supplier-carrierList-create'),
    path('supplier-carriers/<int:pk>', CarrierDetailView.as_view(), name='supplier-carrierDetail'),

    path('suppliers', SupplierListCreateView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>', SupplierDetailView.as_view(), name='supplier-detail'),

    path('supplier-items', SupplierItemListCreateView.as_view(), name='supplier-item-list-create'),
    path('supplier-items/<int:pk>', SupplierItemDetailView.as_view(), name='supplier-item-detail'),

    path('supplier-contacts', SupplierContactListCreateView.as_view(), name='supplier-contact-list-create'),
    path('supplier-contacts/<int:pk>', SupplierContactDetailView.as_view(), name='supplier-contact-detail'),

    path('supplier-shippingitems', ShippingItemCreateView.as_view(), name='supplier-shippingitems-create'),
    path('supplier-shippingitems/<int:pk>', ShippingItemDetailView.as_view(), name='supplier-shippingitems-detail'),

    path('ship-docs', ShipDocsListCreateView.as_view(), name='ship-docs-create'),
    path('ship-docs/<int:pk>', ShipDocsDetailView.as_view(), name='ship-docs-detail'),

    path('supplier-shipping', ShippingListCreateView.as_view(), name='supplier-shipping-create'),
    path('supplier-shipping/<int:pk>', ShippingDetailView.as_view(), name='supplier-shipping-detail'),

    path('supplier-po', SupplierPOListCreateView.as_view(), name='supplier-po-create'),
    path('supplier-po/<int:pk>', SupplierPODetailView.as_view(), name='supplier-po-detail'),
]


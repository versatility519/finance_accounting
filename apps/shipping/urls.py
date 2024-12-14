from django.urls import path
from .views import (
    ShippingListCreateView, ShippingDetailView,
    ShippingItemListCreateView, ShippingItemDetailView,
    NotesListCreateView, NotesDetailView,
    CarrierListCreateView, CarrierDetailView
)

urlpatterns = [
    # Shipping endpoints
    path('shipping', ShippingListCreateView.as_view(), name='shipping-list'),
    path('shipping/<int:pk>', ShippingDetailView.as_view(), name='shipping-detail'),
    
    # Shipping Items endpoints
    path('shipping-items', ShippingItemListCreateView.as_view(), name='shipping-item-list'),
    path('shipping-items/<int:pk>', ShippingItemDetailView.as_view(), name='shipping-item-detail'),
    
    # Notes endpoints
    path('notes', NotesListCreateView.as_view(), name='notes-list'),
    path('notes/<int:pk>', NotesDetailView.as_view(), name='notes-detail'),
    
    # Carrier endpoints
    path('shipping-carriers', CarrierListCreateView.as_view(), name='shipping-carrier-list'),
    path('shipping-carriers/<int:pk>', CarrierDetailView.as_view(), name='shipping-carrier-detail'),
]
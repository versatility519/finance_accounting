from django.urls import path
from .views import (
    SalesListCreateView,
    SalesDetailView,
    SalesItemListCreateView,
    SalesItemDetailView,
)

urlpatterns = [
    path('sales', SalesListCreateView.as_view(), name='sales-list-create'),
    path('sales/<int:pk>', SalesDetailView.as_view(), name='sales-detail'),

    path('sales-items', SalesItemListCreateView.as_view(), name='sales-item-list-create'),
    path('sales-items/<int:pk>', SalesItemDetailView.as_view(), name='sales-item-detail'),
]
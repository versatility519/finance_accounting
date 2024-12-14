from django.urls import path
from .views import (
    TermsListCreateView,
    TermsDetailView,
    
    BillDocListCreateView,
    BillDocDetailView,
    
    BillItemListCreateView,
    BillItemDetailView,
    
    BillListCreateView,
    BillDetailView,
)

urlpatterns = [
    path('bill-terms', TermsListCreateView.as_view(), name='terms-list-create'),
    path('bill-terms/<int:pk>', TermsDetailView.as_view(), name='terms-detail'),

    path('bill-docs', BillDocListCreateView.as_view(), name='bill-doc-list-create'),
    path('bill-docs/<int:pk>', BillDocDetailView.as_view(), name='bill-doc-detail'),
 
    path('bill-item', BillItemListCreateView.as_view(), name='bill-item-list-create'),
    path('bill-item/<int:pk>', BillItemDetailView.as_view(), name='bill-item-detail'),
 
    path('bills', BillListCreateView.as_view(), name='bill-list-create'),
    path('bills/<int:pk>', BillDetailView.as_view(), name='bill-detail'),
]
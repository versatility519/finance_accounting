from django.urls import path
from .views import (
    RequisitionListCreateView,
    RequisitionDetailView,
    RequisitionItemListCreateView,
    RequisitionItemDetailView,
    RequisitionDocListCreateView,
    RequisitionDocDetailView,
)

urlpatterns = [
    path('requisitions', RequisitionListCreateView.as_view(), name='requisition-list-create'),
    path('requisitions/<int:pk>', RequisitionDetailView.as_view(), name='requisition-detail'),
    
    path('requisition-items', RequisitionItemListCreateView.as_view(), name='requisition-item-list-create'),
    path('requisition-items/<int:pk>', RequisitionItemDetailView.as_view(), name='requisition-item-detail'),
   
    path('requisition-docs', RequisitionDocListCreateView.as_view(), name='requisition-doc-list-create'),
    path('requisition-docs/<int:pk>', RequisitionDocDetailView.as_view(), name='requisition-doc-detail'),
]
from django.urls import path
from .views import (
    PdocumentDetailView, 
    PdocumentListCreateView, 
    
    ProductionDetailView,
    ProductionListCreateView,
    
    ProductionItemDetailView,
    ProductionItemListCreateView,
    
)

urlpatterns = [
    path('pdocuments', PdocumentListCreateView.as_view(), name='pdocument-list'),
    path('pdocuments/<int:pk>', PdocumentDetailView.as_view(), name='pdocument-detail'),

    path('productions', ProductionListCreateView.as_view(), name='production-list'),
    path('productions/<int:pk>', ProductionDetailView.as_view(), name='production-detail'),

    path('production-items', ProductionItemListCreateView.as_view(), name='production-item-list'),
    path('production-items/<int:pk>', ProductionItemDetailView.as_view(), name='production-item-detail'),
]
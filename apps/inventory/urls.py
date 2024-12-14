from django.urls import path
from .views import (
    BinListCreateView,
    BinDetailView,

    LocationListCreateView,
    LocationDetailView,
    
    StoreroomDetailView,
    StoreroomListCreateView,

    IssueUnitDetailView, IssueUnitListCreateView,
    OrderUnitDetailView, OrderUnitListCreateView,

    ReceptionDocListCreateView,
    ReceptionDocDetailView,

    ReceptionListCreateView,
    ReceptionDetailView,

    ReceptionItemListCreateView,
    ReceptionItemDetailView,

    ReservationListCreateView,
    ReservationDetailView,

    ReservationItemListCreateView,
    ReservationItemDetailView,
 
    IssueListCreateView,
    IssueDetailView,

    IssueItemListCreateView,
    IssueItemDetailView,

    TransferItemListCreateView,
    TransferItemDetailView,

    TransferListCreateView,
    TransferDetailView,

    InventoryItemListCreateView,
    InventoryItemDetailView,
)

urlpatterns = [
    path('storeroom', StoreroomListCreateView.as_view(), name='storeroom-CreateView-create'),
    path('storeroom/<int:pk>', StoreroomDetailView.as_view(), name='storeroom-detail'),

    path('location', LocationListCreateView.as_view(), name='location-list-create'),
    path('location/<int:pk>', LocationDetailView.as_view(), name='location-detail'),

    path('bins', BinListCreateView.as_view(), name='bin-list-create'),
    path('bins/<int:pk>', BinDetailView.as_view(), name='bin-detail'),
    
    path('reception-docs', ReceptionDocListCreateView.as_view(), name='receptiondoc-list-create'),
    path('reception-docs/<int:pk>', ReceptionDocDetailView.as_view(), name='receptiondoc-detail'),

    path('receptions', ReceptionListCreateView.as_view(), name='reception-list-create'),
    path('receptions/<int:pk>', ReceptionDetailView.as_view(), name='reception-detail'),

    path('reception-items', ReceptionItemListCreateView.as_view(), name='receptionitem-list-create'),
    path('reception-items/<int:pk>', ReceptionItemDetailView.as_view(), name='receptionitem-detail'),

    path('reservations', ReservationListCreateView.as_view(), name='reservation-list-create'),
    path('reservations/<int:pk>', ReservationDetailView.as_view(), name='reservation-detail'), 

    path('reservation-items', ReservationItemListCreateView.as_view(), name='reservationitem-list-create'),
    path('reservation-items/<int:pk>', ReservationItemDetailView.as_view(), name='reservationitem-detail'),  
  
# unit parts
    path('issue-units', IssueUnitListCreateView.as_view(), name='issue-unit-list'),
    path('issue-units/<int:pk>', IssueUnitDetailView.as_view(), name='issue-unit-detail'),

    path('order-units', OrderUnitListCreateView.as_view(), name='order-unit-list'),
    path('order-units/<int:pk>', OrderUnitDetailView.as_view(), name='order-unit-detail'),
    
    path('issues', IssueListCreateView.as_view(), name='issue-list-create'),
    path('issues/<int:pk>', IssueDetailView.as_view(), name='issue-detail'),

    path('issue-items', IssueItemListCreateView.as_view(), name='issueitem-list-create'),
    path('issue-items/<int:pk>', IssueItemDetailView.as_view(), name='issueitem-detail'),

    path('transfert-items', TransferItemListCreateView.as_view(), name='transfertItem-list-create'),
    path('transfert-items/<int:pk>', TransferItemDetailView.as_view(), name='transfertItem-detail'),

    path('transferts', TransferListCreateView.as_view(), name='transfert-list-create'),
    path('transferts/<int:pk>', TransferDetailView.as_view(), name='transfert-detail'),
    
    path('inventory-items', InventoryItemListCreateView.as_view(), name='inventoryitem-list-create'),
    path('inventory-items/<int:pk>', InventoryItemDetailView.as_view(), name='inventoryitem-detail'),
]

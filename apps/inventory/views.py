
from rest_framework import generics

from .models import (
    InventoryItem,
    Reception, ReceptionItem, ReceptionDoc,
    Reservation, ReservationItem,
    Transfert, TransfertItem,
    Issue, IssueItem,
    OrderUnit, IssueUnit,
    Bin, Storeroom, Location
)
from .serializers import (
    InventoryItemSerializer,

    IssueSerializer, IssueItemSerializer,
    OrderUnitSerializer, IssueUnitSerializer,

    TransfertSerializer, TransfertItemSerializer,
    ReceptionSerializer, ReceptionItemSerializer, ReceptionDocSerializer,
    ReservationSerializer, ReservationItemSerializer,
    BinSerializer, LocationSerializer, StoreroomSerializer
)

class TransferItemListCreateView(generics.ListCreateAPIView):
    queryset = TransfertItem.objects.all()
    serializer_class = TransfertItemSerializer

class TransferItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransfertItem.objects.all()
    serializer_class = TransfertItemSerializer

class TransferListCreateView(generics.ListCreateAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer

class TransferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transfert.objects.all()
    serializer_class = TransfertSerializer

class IssueItemListCreateView(generics.ListCreateAPIView):
    queryset = IssueItem.objects.all()
    serializer_class = IssueItemSerializer

class IssueItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssueItem.objects.all()
    serializer_class = IssueItemSerializer

class IssueListCreateView(generics.ListCreateAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class IssueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class ReservationItemListCreateView(generics.ListCreateAPIView):
    queryset = ReservationItem.objects.all()
    serializer_class = ReservationItemSerializer

class ReservationItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReservationItem.objects.all()
    serializer_class = ReservationItemSerializer

class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReceptionDocListCreateView(generics.ListCreateAPIView):
    queryset = ReceptionDoc.objects.all()
    serializer_class = ReceptionDocSerializer

class ReceptionDocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReceptionDoc.objects.all()
    serializer_class = ReceptionDocSerializer

class ReceptionItemListCreateView(generics.ListCreateAPIView):
    queryset = ReceptionItem.objects.all()
    serializer_class = ReceptionItemSerializer

class ReceptionItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReceptionItem.objects.all()
    serializer_class = ReceptionItemSerializer

class ReceptionListCreateView(generics.ListCreateAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer

class ReceptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer

class StoreroomListCreateView(generics.ListCreateAPIView):
    queryset = Storeroom.objects.all()
    serializer_class = StoreroomSerializer

class StoreroomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storeroom.objects.all()
    serializer_class = StoreroomSerializer

class LocationListCreateView(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class BinListCreateView(generics.ListCreateAPIView):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
    
class BinDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bin.objects.all()
    serializer_class = BinSerializer
 
class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    
class OrderUnitListCreateView(generics.ListCreateAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer

class OrderUnitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderUnit.objects.all()
    serializer_class = OrderUnitSerializer

class IssueUnitListCreateView(generics.ListCreateAPIView):
    queryset = IssueUnit.objects.all()
    serializer_class = IssueUnitSerializer

class IssueUnitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IssueUnit.objects.all()
    serializer_class = IssueUnitSerializer
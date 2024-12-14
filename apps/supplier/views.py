from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Carrier, Supplier, SupplierItem, SupplierContact, ShippingItem, ShipDocs, Shipping, SupplierPO
from .serializers import (
    CarrierSerializer, SupplierSerializer, SupplierItemSerializer,
    SupplierContactSerializer, ShippingItemSerializer, ShipDocsSerializer,
    ShippingSerializer, SupplierPOSerializer
)

class CarrierListCreateView(generics.ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

class CarrierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer

class SupplierListCreateView(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class SupplierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class SupplierItemListCreateView(generics.ListCreateAPIView):
    queryset = SupplierItem.objects.all()
    serializer_class = SupplierItemSerializer
    
class SupplierItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierItem.objects.all()
    serializer_class = SupplierItemSerializer

class SupplierContactListCreateView(generics.ListCreateAPIView):
    queryset = SupplierContact.objects.all()
    serializer_class = SupplierContactSerializer

class SupplierContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierContact.objects.all()
    serializer_class = SupplierContactSerializer

class ShippingItemCreateView(generics.ListCreateAPIView):
    queryset = ShippingItem.objects.all()
    serializer_class = ShippingItemSerializer

class ShippingItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingItem.objects.all()
    serializer_class = ShippingItemSerializer

class ShipDocsListCreateView(generics.ListCreateAPIView):
    queryset = ShipDocs.objects.all()
    serializer_class = ShipDocsSerializer

class ShipDocsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShipDocs.objects.all()
    serializer_class = ShipDocsSerializer

class ShippingListCreateView(generics.ListCreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class ShippingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class SupplierPOListCreateView(generics.ListCreateAPIView):
    queryset = SupplierPO.objects.all()
    serializer_class = SupplierPOSerializer

class SupplierPODetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierPO.objects.all()
    serializer_class = SupplierPOSerializer

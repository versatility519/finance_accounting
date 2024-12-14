from rest_framework import generics
from .models import Shipping, ShippingItem, Notes, Carrier
from .serializers import (
    ShippingSerializer, 
    ShippingItemSerializer, 
    NotesSerializer, 
    CarrierSerializer
)

class ShippingListCreateView(generics.ListCreateAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer
    
class ShippingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer

class ShippingItemListCreateView(generics.ListCreateAPIView):
    queryset = ShippingItem.objects.all()
    serializer_class = ShippingItemSerializer
    
class ShippingItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingItem.objects.all()
    serializer_class = ShippingItemSerializer

class NotesListCreateView(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    
class NotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

class CarrierListCreateView(generics.ListCreateAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    
class CarrierDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Carrier.objects.all()
    serializer_class = CarrierSerializer
    
    
    

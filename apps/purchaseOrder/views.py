from rest_framework import generics
from .models import (
    PurchaseDocument, PurchaseOrder, PurchaseOrderItem
)
from .serializers import (
    PurchaseDocumentSerializer, PurchaseOrderSerializer, PurchaseOrderItemSerializer
)

class PurchaseDocumentListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseDocument.objects.all()
    serializer_class = PurchaseDocumentSerializer
    
class PurchaseDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseDocument.objects.all()
    serializer_class = PurchaseDocumentSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    
class PurchaseOrderItemListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    
class PurchaseOrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer

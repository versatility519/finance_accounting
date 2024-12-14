from django.shortcuts import render
from rest_framework import generics
from .models import Sales, SalesItem
from .serializers import (
    SalesSerializer, SalesItemSerializer
)

class SalesListCreateView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)
    #     serializer.save(approved_by=self.request.user)
    #     serializer.save(approved=True)
        
class SalesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class SalesItemListCreateView(generics.ListCreateAPIView):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer

class SalesItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesItem.objects.all()
    serializer_class = SalesItemSerializer
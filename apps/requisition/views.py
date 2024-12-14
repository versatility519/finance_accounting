from django.shortcuts import render
from rest_framework import generics
from .models import (
    Requisition, 
    RequisitionItem, 
    RequisitionDoc
)
from .serializers import (
    RequisitionSerializer, 
    RequisitionItemSerializer, 
    RequisitionDocSerializer
)

class RequisitionListCreateView(generics.ListCreateAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer

class RequisitionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Requisition.objects.all()
    serializer_class = RequisitionSerializer

class RequisitionItemListCreateView(generics.ListCreateAPIView):
    queryset = RequisitionItem.objects.all()
    serializer_class = RequisitionItemSerializer

class RequisitionItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequisitionItem.objects.all()
    serializer_class = RequisitionItemSerializer

class RequisitionDocListCreateView(generics.ListCreateAPIView):
    queryset = RequisitionDoc.objects.all()
    serializer_class = RequisitionDocSerializer

class RequisitionDocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RequisitionDoc.objects.all()
    serializer_class = RequisitionDocSerializer

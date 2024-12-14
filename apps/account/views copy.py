from django.shortcuts import render
from rest_framework import generics
from .models import LedgerAccount, SubSAccount, SubOneAccount, SubTwoAccount, SubThreeAccount
from .serializers import LegerAccountSerializer, SubSAccountSerializer, SubOneAccountSerializer, SubTwoAccountSerializer, SubThreeAccountSerializer

# Create your views here.
class LegerAccountListCreateView(generics.ListCreateAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LegerAccountSerializer

class LegerAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LedgerAccount.objects.all()
    serializer_class = LegerAccountSerializer

class SubSAccountListCreateView(generics.ListCreateAPIView):
    queryset = SubSAccount.objects.all()
    serializer_class = SubSAccountSerializer
    
class SubSAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubSAccount.objects.all()
    serializer_class = SubSAccountSerializer
 
class SubOneAccountListCreateView(generics.ListCreateAPIView):
    queryset = SubOneAccount.objects.all()
    serializer_class = SubOneAccountSerializer

class SubOneAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubOneAccount.objects.all()
    serializer_class = SubOneAccountSerializer
    
class SubTwoAccountListCreateView(generics.ListCreateAPIView):
    queryset = SubTwoAccount.objects.all()
    serializer_class = SubTwoAccountSerializer
    
class SubTwoAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTwoAccount.objects.all()
    serializer_class = SubTwoAccountSerializer
    
class SubThreeAccountListCreateView(generics.ListCreateAPIView):
    queryset = SubThreeAccount.objects.all()
    serializer_class = SubThreeAccountSerializer
    
class SubThreeAccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubThreeAccount.objects.all()
    serializer_class = SubThreeAccountSerializer
    
    

from rest_framework import generics
from .models import TrialBalance
from .serializers import (
    TrialBalanceSerializer
)

class TrialBalanceListCreateView(generics.ListCreateAPIView):
    queryset = TrialBalance.objects.all()
    serializer_class = TrialBalanceSerializer
    
class TrialBalanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrialBalance.objects.all()
    serializer_class = TrialBalanceSerializer
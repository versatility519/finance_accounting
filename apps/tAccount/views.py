from rest_framework import generics
from .models import TAccountTransaction, TAccounts
from .serializers import TAccountTransactionSerializer, TAccountsSerializer

class TAccountsListView(generics.ListCreateAPIView):
    queryset = TAccounts.objects.all()
    serializer_class = TAccountsSerializer

class TAccountsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TAccounts.objects.all()
    serializer_class = TAccountsSerializer
    
class TAccountTransactionListView(generics.ListCreateAPIView):
    queryset = TAccountTransaction.objects.all()
    serializer_class = TAccountTransactionSerializer

class TAccountTransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TAccountTransaction.objects.all()
    serializer_class = TAccountTransactionSerializer
    

from rest_framework import generics
from .models import Journal, Transaction
from .serializers import JournalSerializer, TransactionSerializer

# class JournalCreateView(generics.CreateAPIView):
#     queryset = Journal.objects.all()
#     serializer_class = JournalSerializer

class JournalListView(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
from rest_framework import generics
from .models import Bill, BillItem, Terms, BillDoc
from .serializers import BillSerializer, BillItemSerializer, TermsSerializer, BillDocSerializer
# Create your views here.

class TermsListCreateView(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer

class TermsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer

class BillDocListCreateView(generics.ListCreateAPIView):
    queryset = BillDoc.objects.all()
    serializer_class = BillDocSerializer

class BillDocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillDoc.objects.all()
    serializer_class = BillDocSerializer

class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillItemListCreateView(generics.ListCreateAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer

class BillItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillItem.objects.all()
    serializer_class = BillItemSerializer
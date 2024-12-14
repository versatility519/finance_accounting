from rest_framework import generics
from apps.organization.models import Tax
from .models import Invoice, InvoiceItem, InvoiceDoc, Terms, InvoiceNotes
from .serializers import (
    InvoiceSerializer,
    InvoiceItemSerializer,
    InvoiceDocSerializer,
    TermsSerializer,
    InvoiceNoteSerializer
)

# InvoiceDoc Views
class InvoiceDocListCreateView(generics.ListCreateAPIView):
    queryset = InvoiceDoc.objects.all()
    serializer_class = InvoiceDocSerializer

class InvoiceDocDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDoc.objects.all()
    serializer_class = InvoiceDocSerializer

# Terms Views
class TermsListCreateView(generics.ListCreateAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer

class TermsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Terms.objects.all()
    serializer_class = TermsSerializer

# Invoice Views
class InvoiceListCreateView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

# InvoiceItem Views
class InvoiceItemListCreateView(generics.ListCreateAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

class InvoiceItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceItem.objects.all()
    serializer_class = InvoiceItemSerializer

# Invoice Notes
class InvoiceNotesListCreateView(generics.ListCreateAPIView):
    queryset = InvoiceNotes.objects.all()
    serializer_class = InvoiceNoteSerializer

class InvoiceNotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceNotes.objects.all()
    serializer_class = InvoiceNoteSerializer
from django.db import models
from rest_framework import serializers

from .models import Invoice, InvoiceItem, InvoiceDoc, Terms, InvoiceNotes

from apps.inventory.models import IssueUnit
from apps.inventory.serializers import IssueUnitSerializer

from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer

from apps.organization.models import Tax
from apps.organization.serializers import TaxSerializer

from apps.user.models import User
from apps.user.serializers import UserSerializer

from apps.client.models import Client, Contact
from apps.client.serializers import ClientSerializer, ContactSerializer

class InvoiceDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDoc
        fields = ['id', 'name', 'description', 'doc_file', 'invoice', 'created_at']

    def create(self, validated_data):
        max_id = InvoiceDoc.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        invoice_doc = InvoiceDoc.objects.create(**validated_data)
        return invoice_doc  

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ['id', 'name', 'created_at']
        
    def create(self, validated_data):
        max_id = Terms.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        invoice_term = Terms.objects.create(**validated_data)
        return invoice_term  

class InvoiceItemSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all()) 
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all()) 
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())
    
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    
    class Meta:
        model = InvoiceItem
        fields = ['id', 'name', 'description', 'account', 'measure_unit', 'quantity', 'price', 'net_amount', 'tax_amount', 'tax_group', 'invoice', 'created_at']
    
    def create(self, validated_data):
        max_id = InvoiceItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        invoice_item = InvoiceItem.objects.create(**validated_data)
        return invoice_item  
    
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('net_amount', None)
            self.fields.pop('tax_amount', None)

        if request and request.method == 'PUT':
            self.fields.pop('net_amount', None)
            self.fields.pop('tax_amount', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = IssueUnitSerializer(instance.measure_unit).data
        representation['account'] = LedgerAccountSerializer(instance.account).data
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        return representation

class InvoiceSerializer(serializers.ModelSerializer):
    items =  InvoiceItemSerializer(many=True)
    
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())  
    
    invoiceDocs = InvoiceDocSerializer(many=True)

    class Meta:
        model = Invoice
        fields = [
            'id', 'invoice_num', 'created_date', 'client', 'required_date', 
            'status', 'ship_to', 'bill_to', 'terms', 'total_tax_amount', 'total_net_amount', 'total_amount', 'contact', 'turn_to_pdf', 'client_approval', 'items', 'invoiceDocs'
        ]

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('invoiceDocs', None)
            self.fields.pop('total_tax_amount', None)
            self.fields.pop('total_net_amount', None)
            self.fields.pop('total_amount', None)
        super().__init__(*args, **kwargs)
    
    def create(self, validated_data):
        max_id = Invoice.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        invoice = Invoice.objects.create(**validated_data)
        return invoice  
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = InvoiceItemSerializer(instance.items.all(), many=True).data
        
        representation['invoiceDocs'] = InvoiceDocSerializer(instance.invoiceDocs.all(), many=True).data
        representation['terms'] = TermsSerializer(instance.terms).data
        representation['contact'] = ContactSerializer(instance.contact).data
        representation['client'] = ClientSerializer(instance.client).data
        return representation
    
class InvoiceNoteSerializer(serializers.ModelSerializer):
    invoice = serializers.PrimaryKeyRelatedField(queryset=Invoice.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
       
    class Meta:
        model = InvoiceNotes
        fields = [
            'id', 'user', 'invoice', 'created_at'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = UserSerializer(instance.user.all(), many=True).data
        
        representation['invoice'] = InvoiceDocSerializer(instance.invoice.all(), many=True).data
    
        return representation
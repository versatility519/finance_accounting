from rest_framework import serializers
from django.db import models

from .models import Bill, BillItem, BillDoc, Terms

from apps.inventory.models import OrderUnit
from apps.inventory.serializers import IssueUnitSerializer

from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer

from apps.organization.models import Tax
from apps.organization.serializers import TaxSerializer

from apps.supplier.models import Supplier, SupplierContact
from apps.supplier.serializers import SupplierSerializer, SupplierContactSerializer

class BillDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDoc
        fields = ['id', 'name', 'description', 'doc_file', 'bill', 'created_at']

    def create(self, validated_data):
        max_id = BillDoc.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        bill_doc = BillDoc.objects.create(**validated_data)
        return bill_doc 

class TermsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terms
        fields = ['id', 'name']

    def create(self, validated_data):
        max_id = Terms.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        bill_term = Terms.objects.create(**validated_data)
        return bill_term 

class BillItemSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    
    bill = serializers.PrimaryKeyRelatedField(queryset=Bill.objects.all())

    class Meta:
        model = BillItem
        fields = ['id', 'name', 'description', 'account', 'measure_unit', 'quantity', 'price', 'net_amount', 'tax_amount', 'tax_group', 'bill', 'created_at']

    def create(self, validated_data):
        max_id = BillItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        bill_item = BillItem.objects.create(**validated_data)
        return bill_item 

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('net_amount', None)
            self.fields.pop('tax_amount', None)
        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = IssueUnitSerializer(instance.measure_unit).data
        representation['account'] = LedgerAccountSerializer(instance.account).data
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        return representation

class BillSerializer(serializers.ModelSerializer):
    items = BillItemSerializer(many=True)
    billDocs = BillDocSerializer(many=True)
    
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    contact = serializers.PrimaryKeyRelatedField(queryset=SupplierContact.objects.all())
    
    class Meta:
        model = Bill
        fields = ['id', 'bill_num', 'date_created', 'supplier', 'items', 'required_date', 'status', 'ship_to', 'bill_to', 'total_tax_amount', 'total_net_amount', 'total_amount', 'terms', 'billDocs', 'contact', 'created_at']
        
    def create(self, validated_data):
        max_id = Bill.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        bills = Bill.objects.create(**validated_data)
        return bills 
    
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('billDocs', None)
        super().__init__(*args, **kwargs)
 
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = BillItemSerializer(instance.items.all(), many=True).data
        
        representation['billDocs'] = BillDocSerializer(instance.billDocs.all(), many=True).data
        representation['terms'] = TermsSerializer(instance.terms).data
      
        representation['supplier'] = SupplierSerializer(instance.supplier).data
        representation['contact'] = SupplierContactSerializer(instance.contact).data
        return representation
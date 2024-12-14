from django.db import models
from rest_framework import serializers
from .models import Requisition, RequisitionItem, RequisitionDoc
from apps.organization.models import Tax, Department
from apps.organization.serializers import TaxSerializer, DepartmentSerializer

from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

from apps.supplier.models import Supplier
from apps.supplier.serializers import SupplierSerializer

from apps.inventory.models import OrderUnit
from apps.inventory.serializers import OrderUnitSerializer

class RequisitionDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisitionDoc
        fields = ['id', 'name', 'docs', 'requisition', 'created_at']
    
    def create(self, validated_data):
        max_id = RequisitionDoc.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        requisition_docs = RequisitionDoc.objects.create(**validated_data)
        return requisition_docs

class RequisitionItemSerializer(serializers.ModelSerializer):
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    measureUnit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    requisition = serializers.PrimaryKeyRelatedField(queryset=Requisition.objects.all())
    
    class Meta:
        model = RequisitionItem
        fields = ['id', 'name', 'description', 'measureUnit', 'manufacturer', 'manufacturer_code', 'supplier', 'quantity', 'price', 'net_amount', 'tax_amount', 'tax_group', 'reception_quantity', 'requisition','created_at']
    
    def create(self, validated_data):
        max_id = RequisitionItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        requisition_item = RequisitionItem.objects.create(**validated_data)
        return requisition_item
    
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

        representation['supplier'] = instance.supplier.supplier_name if instance.supplier else None
        representation['measureUnit'] = instance.measureUnit.name if instance.measureUnit else None
        representation['tax_group'] = instance.tax_group.tax_rate if instance.tax_group else None
       
        return representation

class RequisitionSerializer(serializers.ModelSerializer):
    items = RequisitionItemSerializer(many=True)
    
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    approved_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    docs = serializers.PrimaryKeyRelatedField(queryset=RequisitionDoc.objects.all())

    class Meta:
        model = Requisition
        fields = [
            'id', 'requisition_number', 'date', 'docs', 'ship_to', 'bill_to', 'department', 'status', 'approved_by', 'created_by', 'total_net_amount', 'total_tax_amount', 'total_amount', 'items', 'created_at'
            ]

    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('total_tax_amount', None)
            self.fields.pop('total_net_amount', None)
            self.fields.pop('total_amount', None)
        super().__init__(*args, **kwargs)
    
    def create(self, validated_data):
        max_id = Requisition.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        requisition = Requisition.objects.create(**validated_data)
        return requisition
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = RequisitionItemSerializer(instance.items, many=True).data
        representation['department'] = DepartmentSerializer(instance.department).data
        representation['approved_by'] = UserSerializer(instance.approved_by).data
        representation['created_by'] = UserSerializer(instance.created_by).data
    
        representation['docs'] = RequisitionDocSerializer(instance.docs).data

        return representation
from django.db import models
from rest_framework import serializers
from .models import (Shipping, ShippingItem, Notes, Carrier)

from apps.sales.models import Sales
from apps.sales.serializers import SalesSerializer

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id', 'name', 'tracking_url', 'contact_phone', 'is_active']

    def create(self, validated_data):
        max_id = Carrier.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        carrier = Carrier.objects.create(**validated_data)
        return carrier  
    
class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'name', 'created_at']

    def create(self, validated_data):
        max_id = Notes.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        note = Notes.objects.create(**validated_data)
        return note  

class ShippingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingItem
        fields = [
            'id', 
            'item_name',
            'description',
            'manufacturer',
            'manufacturer_code',
            'quantity',
            'shipping',
            'created_at'
        ]
        
    def create(self, validated_data):
        max_id = ShippingItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        shipping_item = ShippingItem.objects.create(**validated_data)
        return shipping_item  
    
class ShippingSerializer(serializers.ModelSerializer):
    items = ShippingItemSerializer(many=True, read_only=True)
    carrier = CarrierSerializer(read_only=True)
    notes = NotesSerializer(read_only=True)
    sales = SalesSerializer(read_only=True)
    sales_id = serializers.PrimaryKeyRelatedField(
        queryset=Sales.objects.all(),
        write_only=True,
        source='sales'
    )
    carrier_id = serializers.PrimaryKeyRelatedField(
        queryset=Carrier.objects.all(),
        write_only=True,
        source='carrier'
    )
    notes_id = serializers.PrimaryKeyRelatedField(
        queryset=Notes.objects.all(),
        write_only=True,
        source='notes'
    )

    class Meta:
        model = Shipping
        fields = [
            'id',
            'shipping_num',
            'shipping_name',
            'notes',
            'notes_id',
            'carrier',
            'carrier_id',
            'sales',
            'sales_id',
            'other',
            'shipping_date',
            'items',
            'created_at'
        ]

    def create(self, validated_data):
        max_id = Shipping.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        shipping = Shipping.objects.create(**validated_data)
        return shipping  
    

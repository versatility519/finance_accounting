from django.db import models
from rest_framework import serializers
from django.apps import apps
from .models import Carrier, Supplier, SupplierItem, SupplierContact, ShippingItem, ShipDocs, Shipping, SupplierPO

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id', 'name', 'created_at']
        
    def create(self, validated_data):
        max_id = Carrier.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        carrier = Carrier.objects.create(**validated_data)
        return carrier  

class SupplierContactSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = SupplierContact
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'role', 'full_name', 'created_at']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

class SupplierItemSerializer(serializers.ModelSerializer):
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=apps.get_model('inventory', 'OrderUnit').objects.all())

    class Meta:
        model = SupplierItem
        fields = ['id', 'item_name', 'description', 'sku', 'manufacturer', 'manufacturer_code', 'quantity', 'measure_unit', 'growth', 'growth_fre', 'growth_per', 'created_at']

    def create(self, validated_data):
        # Calculate the next ID based on the current maximum ID
        max_id = SupplierItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  # Increment the maximum ID by 1
        # Handles recursive creation of sub-accounts
        validated_data['id'] = new_id
        supplier_item = SupplierItem.objects.create(**validated_data)
        return supplier_item
    
    def validate_growth_per(self, value):
        if value < 0:
            raise serializers.ValidationError("Growth percentage cannot be negative.")
        return value

class SupplierSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=apps.get_model('user', 'User').objects.all(), required=False, allow_null=True)
    account = serializers.PrimaryKeyRelatedField(queryset=apps.get_model('account', 'LedgerAccount').objects.all(), required=False, allow_null=True)
    inventory_items = serializers.PrimaryKeyRelatedField(many=True, queryset=apps.get_model('inventory', 'InventoryItem').objects.all(), required=False)
    supplier_items = SupplierItemSerializer(many=True, read_only=True)
    supplier_contact = SupplierContactSerializer(many=True, read_only=True)

    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name', 'address', 'billing_address', 'shipping_address', 'user', 'account', 'inventory_items', 'supplier_items', 'supplier_contact', 'created_at']

    def create(self, validated_data):
        # Calculate the next ID based on the current maximum ID
        max_id = Supplier.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  # Increment the maximum ID by 1
        # Handles recursive creation of sub-accounts
        
        inventory_items = validated_data.pop('inventory_items', [])
        supplier = Supplier.objects.create(id=new_id, **validated_data)
        supplier.inventory_items.set(inventory_items)
        return supplier

class ShippingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingItem
        fields = ['id', 'shipping_name', 'description', 'manufacturer', 'manufacturer_code', 'item_code', 'created_at']

    def create(self, validated_data):
        
        # Calculate the next ID based on the current maximum ID
        max_id = ShippingItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  # Increment the maximum ID by 1
        # Handles recursive creation of sub-accounts
        
        supplier_item = ShippingItem.objects.create(id=new_id, **validated_data)
        return supplier_item
    
class ShipDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShipDocs
        fields = ['id', 'doc_name', 'doc_file', 'created_at']

class ShippingSerializer(serializers.ModelSerializer):
    purchase_order = serializers.PrimaryKeyRelatedField(queryset=apps.get_model('purchaseOrder', 'PurchaseOrder').objects.all())
    sent_by = CarrierSerializer(read_only=True)
    sent_by_id = serializers.PrimaryKeyRelatedField(queryset=Carrier.objects.all(), write_only=True, source='sent_by')
    shipping_items = ShippingItemSerializer(many=True, read_only=True)
    shipping_docs = ShipDocsSerializer(many=True, read_only=True)

    class Meta:
        model = Shipping
        fields = ['id', 'purchase_order', 'sent_by', 'sent_by_id', 'shipping_date', 'ETA', 'shipping_items', 'shipping_docs', 'created_at']

    def create(self, validated_data):
        # Calculate the next ID based on the current maximum ID
        max_id = Shipping.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  # Increment the maximum ID by 1
        # Handles recursive cre
        # ation of sub-accounts
        
        shipping = Shipping.objects.create(id=new_id, **validated_data)
        return shipping

    def validate_ETA(self, value):
        if value < 0:
            raise serializers.ValidationError("ETA cannot be negative.")
        return value

class SupplierPOSerializer(serializers.ModelSerializer):
    purchase_order = serializers.PrimaryKeyRelatedField(queryset=apps.get_model('purchaseOrder', 'PurchaseOrder').objects.all())
    shipping = ShippingSerializer(read_only=True)
    shipping_id = serializers.PrimaryKeyRelatedField(queryset=Shipping.objects.all(), write_only=True, source='shipping')

    class Meta:
        model = SupplierPO
        fields = ['id', 'purchase_order', 'shipping', 'shipping_id', 'sup_approved', 'created_at']

    def create(self, validated_data):
        # Calculate the next ID based on the current maximum ID
        max_id = SupplierPO.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  # Increment the maximum ID by 1
        # Handles recursive creation of sub-accounts
        validated_data['id'] = new_id 
        supplier_po = SupplierPO.objects.create(**validated_data)
        return supplier_po

    def validate(self, data):
        if data['purchase_order'] != data['shipping'].purchase_order:
            raise serializers.ValidationError("The purchase order of the shipping must match the supplier PO's purchase order.")
        return data
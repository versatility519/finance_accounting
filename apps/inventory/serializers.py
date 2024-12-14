from django.db import models
from rest_framework import serializers
from apps.users.models import CustomUser
from apps.users.serializers import UserSerializer

from apps.project.models import Project
from apps.project.serializers import ProjectSerializer

from apps.purchaseOrder.models import PurchaseOrder
# from apps.purchaseOrder.serializers import PurchaseOrderSerializer

from .models import (
    SubCategory,
    InventoryItem,
    Reception, ReceptionItem,
    Reservation, ReservationItem, 
    Transfert, TransfertItem,
    Issue, IssueItem,
    OrderUnit, IssueUnit,
    Bin, ReceptionDoc, Storeroom,Location
)

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'created_at']
        
    def create(self, validated_data):
        max_id = SubCategory.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        sub_category = SubCategory.objects.create(**validated_data)
        return sub_category  

class StoreroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storeroom
        fields = ['id', 'name', 'address', 'bill_to', 'created_at']

    def create(self, validated_data):
        max_id = Storeroom.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        store_room = Storeroom.objects.create(**validated_data)
        return store_room  

class LocationSerializer(serializers.ModelSerializer):
    storeroom = StoreroomSerializer()
    class Meta:
        model = Location
        fields = ['id', 'name', 'storeroom', 'created_at']

    def create(self, validated_data):
        max_id = Location.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        store_location = Location.objects.create(**validated_data)
        return store_location  
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['storeroom'] = StoreroomSerializer(instance.storeroom).data
        return representation
    
class BinSerializer(serializers.ModelSerializer):
    bin_location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())

    class Meta:
        model = Bin
        fields = ['id', 'bin_name', 'bin_location', 'created_at']

    def create(self, validated_data):
        max_id = Bin.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        bin = Bin.objects.create(**validated_data)
        return bin  
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['bin_location'] = LocationSerializer(instance.bin_location).data
        return representation

class OrderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ['id', 'name', 'created_at']

    def create(self, validated_data):
        max_id = OrderUnit.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        order_unit = OrderUnit.objects.create(**validated_data)
        return order_unit  
    
class IssueUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueUnit
        fields = ['id', 'name', 'created_at']

    def create(self, validated_data):
        max_id = IssueUnit.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        issue_unit = IssueUnit.objects.create(**validated_data)
        return issue_unit  

class IssueItemSerializer(serializers.ModelSerializer):
    measureUnit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())

    class Meta:
        model = IssueItem
        fields = ['id', 'item_name', 'item_code', 'item_description', 'item_manufacturer', 'item_manufacturer_code', 'item_quantity', 'measureUnit' ,'created_at']
    
    def create(self, validated_data):
        max_id = IssueItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        issue_item = IssueItem.objects.create(**validated_data)
        return issue_item  
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measureUnit'] = IssueUnitSerializer(instance.measureUnit).data
        return representation
    
class IssueSerializer(serializers.ModelSerializer):
    # items = IssueItemSerializer(many=True)
    items = serializers.PrimaryKeyRelatedField(queryset=IssueItem.objects.all())
    storekeeper = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())

    class Meta:
        model = Issue
        fields = ['id', 'name', 'created_date', 'items', 'reason', 'storekeeper', 'notes', 'project', 'created_at']

    def create(self, validated_data):
        max_id = Issue.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        issues = Issue.objects.create(**validated_data)
        return issues  
          
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['storekeeper'] = UserSerializer(instance.storekeeper).data
        representation['items'] = IssueItemSerializer(instance.items).data 
        representation['project'] = ProjectSerializer(instance.project).data
        return representation

class ReservationItemSerializer(serializers.ModelSerializer):
    measureUnit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())
    
    class Meta:
        model = ReservationItem
        fields = ['id', 'item_name', 'item_description', 'item_code', 'item_manufacturer', 'item_manufacturer_code', 'item_quantity', 'measureUnit', 'created_at']
    
    def create(self, validated_data):
        max_id = ReservationItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        reservation_item = ReservationItem.objects.create(**validated_data)
        return reservation_item 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measureUnit'] = IssueUnitSerializer(instance.measureUnit).data
        return representation

class ReservationSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=ReservationItem.objects.all())
    reserved_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    storekeeper = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    
    class Meta:
        model = Reservation
        fields = ['id', 'items', 'reason', 'reserved_date', 'reserved_by', 'storekeeper', 'status', 'project']

    def create(self, validated_data):
        max_id = Reservation.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        reservation = Reservation.objects.create(**validated_data)
        return reservation 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['storekeeper'] = UserSerializer(instance.storekeeper).data
        representation['items'] = ReservationItemSerializer(instance.items).data
        representation['project'] = ProjectSerializer(instance.project).data
        return representation

class ReceptionDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceptionDoc
        fields = ['id', 'name', 'description', 'doc_file', 'created_at']
        
    def create(self, validated_data):
        max_id = ReceptionDoc.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        reception_doc = ReceptionDoc.objects.create(**validated_data)
        return reception_doc 
        
class ReceptionItemSerializer(serializers.ModelSerializer):
    item_bin = serializers.PrimaryKeyRelatedField(queryset=Bin.objects.all()) 
    
    class Meta:
        model = ReceptionItem
        fields = ['id', 'item_name', 'item_code', 'item_description', 'item_manufacturer', 'item_manufacturer_code', 'item_quantity', 'item_bin', 'created_at']
        
    def create(self, validated_data):
        max_id = ReceptionItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        reception_item = ReceptionItem.objects.create(**validated_data)
        return reception_item 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['item_bin'] = BinSerializer(instance.item_bin).data
        return representation

class ReceptionSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=ReceptionItem.objects.all())
    storekeeper = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    recep_doc = serializers.PrimaryKeyRelatedField(queryset=ReceptionDoc.objects.all())
    purchase_order = serializers.PrimaryKeyRelatedField(queryset=PurchaseOrder.objects.all())
    
    class Meta:
        model = Reception
        fields = ['id', 'po_number', 'items', 'notes', 'storekeeper', 'recep_doc', 'purchase_order']
        read_only = ['date_received', 'date_updated']
        
    def create(self, validated_data):
        max_id = Reception.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        receptions = Reception.objects.create(**validated_data)
        return receptions 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = ReceptionItemSerializer(instance.items).data
        representation['storekeeper'] = UserSerializer(instance.storekeeper).data
        representation['recep_doc'] = ReceptionDocSerializer(instance.recep_doc).data
        # representation['purchase_order'] = PurchaseOrderSerializer(instance.purchase_order).data
        return representation

class TransfertItemSerializer(serializers.ModelSerializer):
    item_bin = serializers.PrimaryKeyRelatedField(queryset=Bin.objects.all()) 
    
    class Meta:
        model = TransfertItem
        fields = ['id', 'item_name', 'item_description', 'item_manufacturer', 'item_manufacCode', 'item_quantity', 'item_bin', 'status', 'created_at']

    def create(self, validated_data):
        max_id = TransfertItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        transfert_item = TransfertItem.objects.create(**validated_data)
        return transfert_item 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['item_bin'] = BinSerializer(instance.item_bin).data
        return representation
    
class TransfertSerializer(serializers.ModelSerializer):
    trans_items = serializers.PrimaryKeyRelatedField(queryset=TransfertItem.objects.all()) 
    created_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    bin = serializers.PrimaryKeyRelatedField(queryset = Bin.objects.all())

    class Meta:
        model = Transfert
        fields = ['id', 'trans_number', 'date', 'trans_items', 'reason', 'created_by', 'status', 'bin', 'created_at']

    def create(self, validated_data):
        max_id = Transfert.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        transferts = Transfert.objects.create(**validated_data)
        return transferts 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['trans_items'] = TransfertItemSerializer(instance.trans_items).data
        representation['created_by'] = UserSerializer(instance.created_by).data
        representation['bin'] = BinSerializer(instance.bin).data
        return representation

class InventoryItemSerializer(serializers.ModelSerializer):
    order_unit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    issue_unit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())
    sub_category = serializers.PrimaryKeyRelatedField(queryset=SubCategory.objects.all())
    bin = serializers.PrimaryKeyRelatedField(queryset=Bin.objects.all())
    
    class Meta:
        model = InventoryItem
        fields = ['id', 'name', 'item_code', 'description', 'order_unit', 'issue_unit', 'manufacturer', 'manufacturer_code', 'price', 'min_quantity', 'max_quantity', 'current_balance', 'physical_count', 'image', 'bin', 'reorder', 'reorder_point', 'reorder_quantity', 'type', 'preferred_supplier', 'suppliers', 'account', 'sub_category', 'created_at']
    
    def create(self, validated_data):
        max_id = InventoryItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        inventory_item = InventoryItem.objects.create(**validated_data)
        return inventory_item 
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['order_unit'] = OrderUnitSerializer(instance.order_unit).data
        representation['issue_unit']=IssueUnitSerializer(instance.issue_unit).data
        representation['sub_category'] = SubCategorySerializer(instance.sub_category).data
        representation['bin'] = BinSerializer(instance.bin).data
        return representation


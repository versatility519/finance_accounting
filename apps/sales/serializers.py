from django.db import models
from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Sales, SalesItem

from apps.user.models import User
from apps.user.serializers import UserSerializer

from apps.inventory.models import IssueUnit
from apps.inventory.serializers import IssueUnitSerializer

from apps.organization.models import Department, Tax
from apps.organization.serializers import DepartmentSerializer, TaxSerializer

from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer


class SalesItemSerializer(serializers.ModelSerializer):
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
    tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    
    class Meta:
        model = SalesItem
        fields = [
            'id', 'item_name', 'description', 'measure_unit', 'manufacturer', 
            'manufacturer_code', 'status', 'quantity', 'price', 'net_amount', 
            'tax_amount', 'tax_group', 'account', 'sales', 'created_at'
        ]

    def create(self, validated_data):
        max_id = SalesItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        sales_item = SalesItem.objects.create(**validated_data)
        return sales_item
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tax_group'] = TaxSerializer(instance.tax_group).data
        representation['account'] = LedgerAccountSerializer(instance.account).data
        representation['measure_unit'] = IssueUnitSerializer(instance.measure_unit).data
        return representation

class SalesSerializer(serializers.ModelSerializer):
    items = SalesItemSerializer(many=True, required=False)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    approved_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Sales
        fields = [
            'id', 'sales_number', 'created_date', 'ship_to', 'bill_to', 
            'department', 'status', 'approved', 'approved_by', 'created_by', 
            'total_net_amount', 'total_tax_amount', 'total_amount', 'items' ,'created_at'
        ]
        
    #  if not request.user.groups.filter(name='Buyer').exists():
    #         raise ValidationError("Only users with the Buyer role can create sales.")
    #     validated_data['created_by'] = request.user
    #     return super().create(validated_data)

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        
        # Get the user from context
        # user = self.context['request'].user
        # if user.is_anonymous:
        #     raise ValidationError("User must be authenticated to create a Sales entry.")
        
        # if not user.groups.filter(name='Buyer').exists():
        #     raise ValidationError("Only users with the Buyer role can create sales.")
        
        max_id = Sales.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        
        validated_data['id'] = new_id
        # Set the created_by field to the authenticated user
        # validated_data['created_by'] = user
        
        # Create Sales instance
        sales = Sales.objects.create(**validated_data)
        
        # Create associated SalesItem instances
        for item_data in items_data:
            SalesItem.objects.create(sales=sales, **item_data)
        
        return sales

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        if items_data is not None:
            instance.items.all().delete()
            for item_data in items_data:
                SalesItem.objects.create(sales=instance, **item_data)
        
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['items'] = SalesItemSerializer(instance.items.all(), many=True).data
        representation['department'] = DepartmentSerializer(instance.department).data
        representation['approved_by'] = UserSerializer(instance.approved_by).data if instance.approved_by else None
        representation['created_by'] = UserSerializer(instance.created_by).data
        return representation



# class SalesItemSerializer(serializers.ModelSerializer):
#     measure_unit = serializers.PrimaryKeyRelatedField(queryset=IssueUnit.objects.all())
#     account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
#     tax_group = serializers.PrimaryKeyRelatedField(queryset=Tax.objects.all())
    
#     class Meta:
#         model = SalesItem
#         fields = ['id', 'item_name', 'description', 'measure_unit', 'manufacturer', 'manufacturer_code', 'status', 'quantity', 'price', 'net_amount', 'tax_amount', 'tax_group', 'account', 'sales']
        
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['tax_group'] = TaxSerializer(instance.tax_group).data
#         representation['account'] = LedgerAccountSerializer(instance.account).data
#         representation['measure_unit'] = IssueUnitSerializer(instance.measure_unit).data
#         return representation

# class SalesSerializer(serializers.ModelSerializer):
#     items = SalesItemSerializer(many=True)
#     department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
#     approved_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
#     class Meta:
#         model = Sales
#         fields = [
#             'id', 'sales_number', 'created_date', 'ship_to', 'bill_to', 'department', 'status', 'approved', 'approved_by', 'created_by', 'total_net_amount', 'total_tax_amount', 'total_amount', 'items'
#             ]
        
#     def __init__(self, *args, **kwargs):
#         request = kwargs.get('context', {}).get('request', None)
#         if request and request.method == 'POST':
#             self.fields.pop('items', None)
#         super().__init__(*args, **kwargs)
        
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['items'] = SalesItemSerializer(instance.items, many=True).data
#         representation['department'] = DepartmentSerializer(instance.department).data
#         representation['approved_by'] = UserSerializer(instance.approved_by).data
#         representation['created_by'] = UserSerializer(instance.created_by).data
    
#         return representation
    

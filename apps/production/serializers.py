from django.db import models
from rest_framework import serializers
from .models import Production, ProductionItem, Pdocument

from apps.project.models import Project
from apps.project.serializers import ProjectSerializer

from apps.inventory.models import OrderUnit
from apps.inventory.serializers import OrderUnitSerializer

class PdocumentSerializer(serializers.ModelSerializer):
    production = serializers.PrimaryKeyRelatedField(queryset=Production.objects.all())
    class Meta:
        model = Pdocument
        fields = ['id', 'doc_name', 'description', 'doc_file', 'production', 'created_at']

    def create(self, validated_data):
        max_id = Pdocument.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        production_doc = Pdocument.objects.create(**validated_data)
        return production_doc     
     
class ProductionItemSerializer(serializers.ModelSerializer):
    measure_unit = serializers.PrimaryKeyRelatedField(queryset=OrderUnit.objects.all())
    class Meta:
        model = ProductionItem
        fields = [
            'id', 'name', 'description', 'quantity', 'manufacturer', 'manufacturer_code', 'measure_unit', 'approved', 'approved_quantity', 'status', 'production', 'created_at'
            ]
    
    def create(self, validated_data):
        max_id = ProductionItem.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        production_item = ProductionItem.objects.create(**validated_data)
        return production_item   
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['measure_unit'] = OrderUnitSerializer(instance.measure_unit).data
        return representation
    
class ProductionSerializer(serializers.ModelSerializer):
    items = ProductionItemSerializer(many=True, required=False)
    docs = PdocumentSerializer(many=True, required=False)

    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    
    class Meta:
        model = Production
        fields = [
            'id', 'p_name', 'project', 'date', 'p_start_date', 'p_end_date', 'p_status', 'approved', 'approved_by', 'items', 'docs'
        ]
    
    def __init__(self, *args, **kwargs):
        request = kwargs.get('context', {}).get('request', None)
        if request and request.method == 'POST':
            self.fields.pop('items', None)
            self.fields.pop('documents', None)
        super().__init__(*args, **kwargs)

    def create(self, validated_data):
        max_id = Production.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        production = Production.objects.create(**validated_data)
        return production  
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)        
        representation['project'] = ProjectSerializer(instance.project).data
        representation['items'] = ProductionItemSerializer(instance.items.all(), many=True).data
        representation['documents'] = PdocumentSerializer(instance.documents.all(), many=True).data
        
        return representation

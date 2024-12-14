from django.db import models
from rest_framework import serializers
from .models import Organization, Tax, Department

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'created_at']
    
    def create(self, validated_data):
        max_id = Department.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        department = Department.objects.create(**validated_data)
        return department  
        
class TaxSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    
    class Meta:
        model = Tax
        fields = ['id', 'tax_name', 'tax_rate', 'description', 'organization', 'created_at']
            
    def create(self, validated_data):
        max_id = Tax.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        tax = Tax.objects.create(**validated_data)
        return tax  
     
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['organization'] = OrganizationSerializer(instance.organization).data
        return representation
        
class OrganizationSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    
    class Meta:
        model = Organization
        fields = ['id', 'name', 'address', 'department', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        max_id = Organization.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        organization = Organization.objects.create(**validated_data)
        return organization  
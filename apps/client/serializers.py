from django.db import models
from rest_framework import serializers
from .models import Client, Contact

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'address', 'user', 'billing_address', 'shipping_address', 'created_at']

    def create(self, validated_data):
        max_id = Client.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        clients = Client.objects.create(**validated_data)
        return clients 

class ContactSerializer(serializers.ModelSerializer):
    clients = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'phone', 'email', 'address', 'role', 'clients', 'created_at']

    def create(self, validated_data):
        max_id = Contact.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        contacts = Contact.objects.create(**validated_data)
        return contacts 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['clients'] = instance.clients.name if instance.clients else None
        
        return representation
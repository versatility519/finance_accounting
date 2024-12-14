from django.db import models
from rest_framework import serializers
from .models import LedgerAccount, SubAccount

class SubAccountSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    class Meta:
        model = SubAccount
        fields = ['id', 'name', 'parent', 'children', 'created_at']

    def get_children(self, instance):
        # Query the related `children` objects and use the same serializer recursively
        children = instance.children.all()
        return SubAccountSerializer(children, many=True).data

    def create(self, validated_data):
        max_id = SubAccount.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  
        # Handles recursive creation of sub-accounts
        children_data = validated_data.pop('children', [])
        sub_account = SubAccount.objects.create(id=new_id, **validated_data)
        
        # Create each child recursively
        for child_data in children_data:
            child_data['parent'] = sub_account  # Set the parent to the current sub-account
            self.create(child_data)  # Recursive call for nested children

        return sub_account

class LedgerAccountSerializer(serializers.ModelSerializer):
    sub_accounts = SubAccountSerializer(many=True, required=False)

    class Meta:
        model = LedgerAccount
        fields = ['id', 'ledger_name', 'account_type', 'type_status', 'sub_accounts', 'created_at']

    def create(self, validated_data):
        max_id = LedgerAccount.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1 

        # Handle sub_accounts creation
        sub_accounts_data = validated_data.pop('sub_accounts', [])
        for sub_account_data in sub_accounts_data:
            sub_account_data['ledger_account'] = ledger_account  # Link to the ledger account
            SubAccountSerializer().create(sub_account_data)  # Create sub-account

        # Create the new LedgerAccount instance with the calculated ID
        ledger_account = LedgerAccount(id=new_id, **validated_data)
        ledger_account.save()
        
        return ledger_account

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sub_accounts'] = SubAccountSerializer(instance.sub_accounts.filter(parent=None), many=True).data
        
        return representation
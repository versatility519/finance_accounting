from django.db import models
from rest_framework import serializers
from .models import TAccountTransaction, TAccounts
from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer
from apps.journal.models import Transaction
from apps.journal.serializers import TransactionSerializer

class TAccountTransactionSerializer(serializers.ModelSerializer):
    transaction = serializers.PrimaryKeyRelatedField(queryset=Transaction.objects.all())
    transaction_account = serializers.CharField(max_length=50, read_only=True)
    
    class Meta:
        model = TAccountTransaction
        fields = ['id', 'date', 'transaction', 'transaction_account', 'debit_amount', 'credit_amount', 'created_at']
        
    def create(self, validated_data):
        max_id = TAccountTransaction.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  
        validated_data['id'] = new_id
        
        t_Account_transaction = TAccountTransaction.objects.create(**validated_data)
        return t_Account_transaction

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['transaction'] = TransactionSerializer(instance.transaction).data
        return representation

class TAccountsSerializer(serializers.ModelSerializer):
    # account = LedgerAccountSerializer(read_only=True)
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
    transaction = serializers.PrimaryKeyRelatedField(queryset=TAccountTransaction.objects.all())
    
    class Meta:
        model = TAccounts
        fields = ['id', 'account', 'transaction', 'total_debit', 'total_credit', 'balance', 'created_at']
    
    def create(self, validated_data):
        max_id = TAccounts.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  
        validated_data['id'] = new_id
        
        t_Account = TAccounts.objects.create(**validated_data)
        return t_Account
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['account'] = LedgerAccountSerializer(instance.account).data
        representation['transaction'] = TAccountTransactionSerializer(instance.transaction).data
        return representation

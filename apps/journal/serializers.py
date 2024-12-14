from django.db import models
from rest_framework import serializers
from .models import Journal, Transaction
from apps.account.models import LedgerAccount
from apps.account.serializers import LedgerAccountSerializer

class TransactionSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=LedgerAccount.objects.all())
    journal = serializers.PrimaryKeyRelatedField(queryset=Journal.objects.all())
    
    class Meta:
        model = Transaction
        fields = ['id', 't_name', 't_date', 't_amount', 't_description', 't_type', 'account', 'journal', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['account'] = instance.account.ledger_name if instance.account else None
        # representation['account'] = LedgerAccountSerializer(instance.account).data
        
        return representation
 
    def create(self, validated_data):
        max_id = Transaction.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1  
        validated_data['id'] = new_id
        
        account = validated_data.get('account')
        
        journal_transction = Transaction.objects.create(**validated_data)
        return journal_transction
    
    def update(self, instance, validated_data):
        account = validated_data.get('account')
        if account:
            instance.account = account

        instance.t_name = validated_data.get('t_name', instance.t_name)
        instance.t_amount = validated_data.get('t_amount', instance.t_amount)
        instance.t_description = validated_data.get('t_description', instance.t_description)
        instance.t_type = validated_data.get('t_type', instance.t_type)
        instance.save()
        return instance
    
class JournalSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)
    # transactions = TransactionSerializer(read_only=True)
    # transactions_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Transaction.objects.all(), 
    #     write_only=True,
    #     source='transactions'
    # )
    total_debit = serializers.SerializerMethodField()
    total_credit = serializers.SerializerMethodField()

    class Meta:
        model = Journal
        fields = ['id', 'name', 'status', 's_date', 'e_date', 'number', 'transactions', 'total_debit', 'total_credit', 'created_at']

    def create(self, validated_data):
        max_id = Journal.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        journal = Journal.objects.create(**validated_data)
        return journal

    def get_total_debit(self, obj):
        return obj.total_debit

    def get_total_credit(self, obj):
        return obj.total_credit

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.number = validated_data.get('number', instance.number)
        instance.save()

        transactions_data = validated_data.pop('transactions', [])
        for transaction_data in transactions_data:
            transaction_id = transaction_data.get('id', None)
            if transaction_id:
                transaction = Transaction.objects.get(id=transaction_id)
                transaction.t_name = transaction_data.get('t_name', transaction.t_name)
                transaction.t_amount = transaction_data.get('t_amount', transaction.t_amount)
                transaction.t_description = transaction_data.get('t_description', transaction.t_description)
                transaction.t_type = transaction_data.get('t_type', transaction.t_type)
                transaction.save()
            else:
                Transaction.objects.create(journal=instance, **transaction_data)
        return instance
from django.db import models
from rest_framework import serializers
from .models import Statement, StatementCategory
from apps.account.models import LedgerAccount

class LedgerAccountMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount
        fields = ['id', 'ledger_name', 'account_type']

class StatementCategorySerializer(serializers.ModelSerializer):
    accounts = LedgerAccountMinimalSerializer(many=True, read_only=True)
    account_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        write_only=True,
        queryset=LedgerAccount.objects.all(),
        source='accounts'
    )

    class Meta:
        model = StatementCategory
        fields = [
            'id', 
            'category_name', 
            'accounts',
            'account_ids',
            'total_amount',
            'created_at',
            'updated_at'
        ]

    
class StatementListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.category_name', read_only=True)

    class Meta:
        model = Statement
        fields = [
            'id',
            'date',
            'statement_name',
            'category',
            'category_name',
            'grand_total',
            'created_at',
            'updated_at'
        ]

class StatementDetailSerializer(serializers.ModelSerializer):
    category = StatementCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=StatementCategory.objects.all(),
        source='category'
    )

    class Meta:
        model = Statement
        fields = [
            'id',
            'date',
            'statement_name',
            'category',
            'category_id',
            'grand_total',
            'created_at',
            'updated_at'
        ]

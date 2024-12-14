from django.db import models
from rest_framework import serializers
from .models import TrialBalance
from apps.tAccount.models import TAccounts

class TrialBalanceSerializer(serializers.ModelSerializer):
    t_account = serializers.PrimaryKeyRelatedField(queryset=TAccounts.objects.all())
    
    class Meta:
        model = TrialBalance
        fields = [
            'id',
            'date',
            't_account',
            'total_debit',
            'total_credit',
            'created_at'
        ]
        
    def create(self, validated_data):
        max_id = TrialBalance.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        trial_balance = TrialBalance.objects.create(**validated_data)
        return trial_balance
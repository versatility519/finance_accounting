from django.shortcuts import render
from django.db import models
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum
from .models import Statement, StatementCategory
from .serializers import (
    StatementListSerializer,
    StatementDetailSerializer,
    StatementCategorySerializer
)

# Create your views here.

class StatementCategoryViewSet(viewsets.ModelViewSet):
    queryset = StatementCategory.objects.all()
    serializer_class = StatementCategorySerializer
    
    def perform_create(self, serializer):
        max_id = StatementCategory.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        serializer.validated_data['id'] = new_id
        category = serializer.save()
        self._update_total_amount(category)

    def perform_update(self, serializer):
        category = serializer.save()
        self._update_total_amount(category)

    def _update_total_amount(self, category):
        total = category.statements.aggregate(
            total=Sum('grand_total')
        )['total'] or 0
        category.total_amount = total
        category.save()

class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return StatementListSerializer
        return StatementDetailSerializer

    def perform_create(self, serializer):
        statement = serializer.save()
        self._update_category_total(statement.category)

    def perform_update(self, serializer):
        old_category = None
        if self.get_object():
            old_category = self.get_object().category

        statement = serializer.save()
        self._update_category_total(statement.category)
        
        if old_category and old_category != statement.category:
            self._update_category_total(old_category)

    def perform_destroy(self, instance):
        category = instance.category
        instance.delete()
        self._update_category_total(category)

    def _update_category_total(self, category):
        total = category.statements.aggregate(
            total=Sum('grand_total')
        )['total'] or 0
        category.total_amount = total
        category.save()

    @action(detail=False, methods=['get'])
    def summary(self):
        statements = self.get_queryset()
        total = statements.aggregate(
            total=Sum('grand_total')
        )['total'] or 0
        
        return Response({
            'total_statements': statements.count(),
            'grand_total': total
        })

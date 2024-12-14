from django.db import models
from rest_framework import serializers
from apps.project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'description', 'start_date', 'end_date', 'budget', 'status', 'created_at']

    def create(self, validated_data):
        max_id = Project.objects.aggregate(max_id=models.Max('id'))['max_id'] or 0
        new_id = max_id + 1
        validated_data['id'] = new_id
        project = Project.objects.create(**validated_data)
        return project      
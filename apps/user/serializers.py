from django.db import models
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from apps.organization.models import Organization

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type": "password"})

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email", "password", "password2", "role", "organization")
        extra_kwargs = {
            "password": {"write_only": True},
            "password2": {"write_only": True}
        }
    def validate_organization(self, value):
        try:
            return Organization.objects.get(name=value)
        except Organization.DoesNotExist:
            raise serializers.ValidationError("Organization does not exist.")
        
    def create(self, validated_data):
        
        count = get_user_model().objects.count()
        new_id = count + 1
        
        organization = validated_data.pop('organization')
        user = get_user_model()(
            id=new_id,
            email=self.validated_data["email"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
            role=self.validated_data["role"],
            organization=organization
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]

        
        if password != password2:
            raise serializers.ValidationError(
                {"password": "Passwords do not match!"})

        user.set_password(password)
        user.save()

        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "email", "role", "is_staff", "first_name", "last_name")

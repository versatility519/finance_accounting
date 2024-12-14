
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser as User
from django.contrib.auth.models import Group
from apps.organization.models import Organization

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role', 'organization']
        
    def validate_organization(self, value):
        try:
            return Organization.objects.get(name=value)
        except Organization.DoesNotExist:
            raise serializers.ValidationError("Organization does not exist.")
        
    def create(self, validated_data):
        organization = validated_data.pop('organization')
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            role=validated_data['role'],
            organization=organization
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class SigninSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        print(f"Attempting to authenticate user: {username}")
        print(f"Password length: {len(password)}")

        if username and password:
            user = authenticate(username=username, password=password)
            
            print('=======>', user)
            
            if user is not None:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError("User account is disabled.")
            # if user:
            #     if user.is_active:
            #         data['user'] = user
            #     else:
            #         raise serializers.ValidationError("User account is disabled.")
            # else:
            #     raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")
        
        return data
        
# class SigninSerializer(serializers.Serializer):
    
#     # username = serializers.CharField(required=True)
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(write_only=True, required=True)
#     print("respond data", serializers)
    
#     def validate(self, data):
#         user = authenticate(email=data['email'], password=data['password'])
        
#         print("====>", user)
        
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Invalid credentials or account is inactive.")

from rest_framework.settings import api_settings
from rest_framework import serializers
from django.contrib.auth import get_user_model  
from .models import User, UserManager


class UserSerializer(serializers.ModelSerializer):
    following = serializer(many=True)
    class Meta:
        model = User 
        fields = (
            'id', 
            'email', 
            'username',
            'firstName', 
            'lastName', 
            'birthday', 
            'password', 
            'following', 
            'is_active',
            'is_staff',
            'date_joined'
        )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
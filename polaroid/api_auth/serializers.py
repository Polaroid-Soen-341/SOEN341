from rest_framework.settings import api_settings
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import User, UserManager


class SubUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')


class UserSerializer(serializers.ModelSerializer):
    following = SubUserSerializer(many=True, required=False)
    followers = SubUserSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'password',
            'following',
            'followers'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

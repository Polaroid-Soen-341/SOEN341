from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from . import serializers

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )

class UserAuth(generics.ListAPIView):
    queryset = User.objects.all().order_by('first_name')
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class GetUsers(generics.ListAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )

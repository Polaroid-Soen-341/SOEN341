from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth import get_user_model
from . import serializers
from .models import User


class GenericUserView():
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return User.objects.all()

class UserCreate(GenericUserView, generics.CreateAPIView):
    permission_classes = (AllowAny, )

class UserAuth(GenericUserView, generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

class GetUsers(GenericUserView, generics.ListAPIView):
    permission_classes = (AllowAny, )

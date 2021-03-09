from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from . import serializers
from api_auth.serializers import RegisterUserSerializer, UserProfileSerializer
from .models import PolaroidUser
# from django.contrib.auth import authenticate
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authtoken.models import Token
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.status import (
#     HTTP_400_BAD_REQUEST,
#     HTTP_404_NOT_FOUND,
#     HTTP_200_OK
# )
# from rest_framework.response import Response

class UserCreate(generics.CreateAPIView):
    queryset = PolaroidUser.objects.all()
    serializer_class = serializers.RegisterUserSerializer
    permission_classes = (AllowAny, )

class UserAuth(generics.ListAPIView):
    queryset = PolaroidUser.objects.all().order_by('fullname')
    serializer_class = serializers.RegisterUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'},
#                         status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)
#     if not user:
#         return Response({'error': 'Invalid Credentials'},
#                         status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key},
#                     status=HTTP_200_OK)
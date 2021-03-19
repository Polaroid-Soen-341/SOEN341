from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
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


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def follow_user(request, username):
    instance = request.user
    user_to_follow = User.objects.filter(username=username)
    if user_to_follow == None:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    following = instance.following.all()
    if user_to_follow[0] not in following:
        instance.following.add(user_to_follow[0])
    else:
        instance.following.remove(user_to_follow[0])

    serializer = serializers.UserSerializer(instance, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=False):
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class GetFollowingUser(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return self.request.user.following.all()

class GetFollowingUsers(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def get_queryset(self):
        return User.objects.filter(username=self.kwargs['pk'])[0].following.all()
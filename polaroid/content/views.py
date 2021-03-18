from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from . import serializers
from . import models
from .permissions import IsOwnerOrReadOnly

class GenericContentListCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_base_model(self):
        raise NotImplementedError()

    def get_queryset(self):
        queryset = self.get_base_model().objects.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostListCreate(GenericContentListCreate):
    serializer_class = serializers.PostSerializer
    def get_base_model(self):
        return models.Post
    
class CommentListCreate(GenericContentListCreate):
    serializer_class = serializers.CommentSerializer
    def get_base_model(self):
        return models.Comment

class PicturesListCreate(GenericContentListCreate):
    serializer_class = serializers.PictureSerializer
    def get_base_model(self):
        return models.Picture

class GenericContentView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_base_model(self):
        raise NotImplementedError()

    def get_queryset(self):
        queryset = self.get_base_model().objects.filter(id=self.kwargs['pk'])
        return queryset

class PostInfo(GenericContentView):
    serializer_class = serializers.PostSerializer
    def get_base_model(self):
        return models.Post

class CommentInfo(GenericContentView):
    serializer_class = serializers.CommentSerializer
    def get_base_model(self):
        return models.Comment

class PictureInfo(GenericContentView):
    serializer_class = serializers.PictureSerializer
    def get_base_model(self):
        return models.Picture
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from . import serializers
from . import models
from .permissions import IsOwnerOrReadOnly

class GenericContent(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = self.base_model.objects.filter(id=self.kwargs['pk'])
        return queryset

class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostInfo(GenericContent):
    base_model = models.Post
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer

class CommentInfo(GenericContent):
    base_model = models.Comment
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

class PictureInfo(generics.RetrieveUpdateDestroyAPIView):
    base_model = models.Picture
    queryset = models.Picture.objects.all()
    serializer_class = serializers.PictureSerializer
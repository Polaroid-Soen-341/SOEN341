from django.contrib.auth.models import User, Group
from .models import Post, Comment
from api_auth.serializers import UserSerializer
from rest_framework import serializers
        
class CommentSerializer(serializers.ModelSerializer):
    like = UserSerializer(read_only = True, many = True)
    class Meta:
        model = Comment
        fields = ['post', 'content', 'date', 'id', 'parent_comment','like']
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'description', 'date', 'id', "comments", "picture"]

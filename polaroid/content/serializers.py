from django.contrib.auth.models import User, Group
from .models import Post, Comment
from rest_framework import serializers

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'content', 'date', 'id']
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'description', 'date', 'id', "comments", "picture"]
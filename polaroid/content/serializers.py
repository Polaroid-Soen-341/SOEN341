from django.contrib.auth.models import User, Group
from .models import Post, Comment, Picture
from rest_framework import serializers

        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'content', 'date', 'id', 'parent_comment', 'likes']
        
class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['post', 'title', 'date', 'picture', 'id']
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    pictures = PictureSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['title', 'content', 'likes', 'date', 'id', "comments", "pictures"]
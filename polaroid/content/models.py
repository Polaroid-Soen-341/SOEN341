from django.db import models
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    title           = models.CharField(max_length=100, null=True)
    description     = models.TextField(null=True)
    date            = models.DateTimeField(auto_now_add=True)
    owner           = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=False)
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content         = models.TextField(null=True)
    date            = models.DateTimeField(auto_now_add=True)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name="comments")
    owner           = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=False)
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.content

class Picture(models.Model):
    title           = models.CharField(max_length=100, null=True)
    picture         = models.ImageField(null=True)
    date            = models.DateTimeField(auto_now_add=True)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, related_name="pictures")
    owner           = models.ForeignKey(User, related_name='pictures', on_delete=models.CASCADE, null=False)
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title
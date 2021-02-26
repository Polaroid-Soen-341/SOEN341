from django.db import models
import uuid


class Post(models.Model):
    title           = models.CharField(max_length=100, null=True)
    content         = models.TextField(null=True)
    date            = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content         = models.TextField(null=True)
    date            = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)

    def _str_(self):
        return self.date

class Picture(models.Model):
    title           = models.CharField(max_length=100, null=True)
    picture         = models.ImageField(null=True)
    date            = models.DateTimeField(auto_now_add=True)
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title
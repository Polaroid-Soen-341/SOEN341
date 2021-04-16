from django.db import models
from api_auth.models import User
import uuid


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    like = models.ManyToManyField(User, related_name='post_likes', blank=False)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, null=False)
    picture = models.ImageField(null=True, blank=True, upload_to="pictures/")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.title)


class Comment(models.Model):
    content = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, related_name="replies",
                                       null=True, blank=True)
    like = models.ManyToManyField(User, related_name='comment_likes', blank=False)
    owner = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, null=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return str(self.content)

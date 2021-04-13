from django.test import TestCase
from api_auth.models import User
from .models import *

# Create your tests here.
class PostCreationTestCase(TestCase):
    def setUp(self):
        owner = User.objects.create_user("admin", "adminadmin.com", "pass")
        Post.objects.create(title="Post 1", description="whatever", owner=owner)

    def test_post_were_created(self):
        """Test if posts were created correctly"""
        post = Post.objects.get(title="Post 1")
        self.assertEqual(post.description, "whatever", "Post 1 Created")
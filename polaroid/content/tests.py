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

    def test_post_title_limit(self):
        #limit = 100 char
        owner = User.objects.create_user("admin", "adminadmin.com", "pass")
        toolong= 'x'*120
        post = Post.objects.create(title=toolong, description="whatever", owner=owner)



        
class CommentCreationTestCase(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user("admin", "adminadmin.com", "pass")
        post=Post.objects.create(title="Post 1", description="whatever", owner=self.owner)
        Comment.objects.create(content="Lorem Ipsum",post=post,owner=self.owner)
        
    def test_comment_was_created(self):
        comment = Comment.objects.get(post= Post.objects.get(title="Post 1"))
        self.assertEqual(comment.content,"Lorem Ipsum", "comment created")

# class FollwingTestCase(TestCase):
#     def setUp(self):
#         user1= User.objects.create_user("user1", "user1@user.com", "userpass")
#         user2= User.objects.create_user("user2", "user2@user.com", "userpass")

#     def Test_use_can_follow(self):

#         #make user1 follow user2 them follow
#         #assert user1 follows user2
#         #assert user2 does not follow user1
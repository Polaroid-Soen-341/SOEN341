from django.test import TestCase
from ptest.ptest import PolaroidUserTest
from api_auth.models import User, UserManager
from api_auth.views import follow_user, GetFollowingUser
from api_auth.serializers import UserSerializer
from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer


class PostCreationTestCase(PolaroidUserTest):
    """Testing Post model"""
    def setUp(self):
        self.create_default_test_user("pctc")
        self.owner = User.objects.get(username="pctc")
        Post.objects.create(title="post_test" , description="whatever", owner=self.owner)

    def test_post_were_created(self):
        """Test if posts were created correctly"""
        self.post = Post.objects.get(title="post_test" )
        self.assertEqual(self.post.description, "whatever", "post_test Created")

    def test_post_title_limit(self):
        """Test posts title limit"""
        #limit = 100 char
        toolong= 'x'*120
        post = Post()
        try:
            post = Post.objects.create(title=toolong, description="whatever", owner=self.owner)
        except Exception as e:
            post = None
        self.assertIsNot(post, None, "Object was created with title of lenght " + str(len(toolong)))
        assert post != None
        #post should not be created
    
    # def test_post_serializer(self):
    #     """Test posts serializer"""
    #     post = Post.objects.get(title="post_test")
    #     ps = PostSerializer(data=post)
    #     self.assertEqual(ps.is_valid(raise_exception=True), True)
    # self.assertEqual(self.Post_serializer.Meta["title"],self.post.title)
    # self.assertEqual(self.Post_serializer.Meta["content"],self.post.content)
    # self.assertEqual(self.Post_serializer.Meta["owner"],self.post.owner)

class CommentCreationTestCase(TestCase):
    """Testing comment model"""
    def setUp(self):
        self.owner = User.objects.create_user("CommentCreationTestCase", "CommentCreationTestCase@admin.com", "pass")
        post=Post.objects.create(title="comment_test", description="whatever", owner=self.owner)
        Comment.objects.create(content="Lorem Ipsum",post=post,owner=self.owner)
        
    def test_comment_was_created(self):
        """Test comment creation"""
        self.comment = Comment.objects.get(post= Post.objects.get(title="comment_test"))
        self.assertEqual(self.comment.content,"Lorem Ipsum", "comment created")

class ContentModelSerializersTestCase(PolaroidUserTest):
    def setUp(self):
        self.owner = self.create_default_test_user("cmstc")
        self.post = Post.objects.create(title="post_test" , description="whatever", owner=self.owner)
    
    def test_post_creation_on_serializer(self):
        """Test post creation serializer"""
        data = {
            'title': "test post", 
            'description' : "test post", 
            'owner': UserSerializer(self.owner)
        }
        ps = PostSerializer(data=data)
        self.assertEqual(ps.is_valid(raise_exception=False), True)

    def test_comment_creation_on_serializer(self):
        """Test comment creation serializer"""
        data = {
            'content' : "test comment", 
            'owner': UserSerializer(self.owner),
            'post' : PostSerializer(self.post)
        }
        ser = PostSerializer(data=data)
        self.assertEqual(ser.is_valid(raise_exception=False), True)
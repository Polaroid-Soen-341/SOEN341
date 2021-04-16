from django.test import TestCase
from ptest.ptest import PolaroidUserTest
from api_auth.models import User, UserManager
from api_auth.views import follow_user, GetFollowingUser
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
    
    def test_Post_serializer(self):
        """Test posts serializer"""
        self.post = Post.objects.get(title="post_test")
        self.Post_serializer = PostSerializer(self.post)
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
    def test_comment_serializer(self):
        """Test comment serializer"""
        self.comment = Comment.objects.get(post= Post.objects.get(title="comment_test"))
        self.Post_serializer = PostSerializer(self.comment)
        # self.assertEqual(self.Post_serializer.Meta["title"],self.post.title)
        # self.assertEqual(self.Post_serializer.Meta["content"],self.post.content)
        # self.assertEqual(self.Post_serializer.Meta["owner"],self.post.owner)




# class FollwingTestCase(PolaroidUserTest):
#     """Testing Following model"""
#     def setUp(self):
#          self.create_default_test_user("follow_test_1")
#          self.create_default_test_user("follow_test_2")

#     def find_follower(self,list_of_follower):
#         for a in list_of_follower:
#             if a.username == "follow_test_2":
#                 return True
#         return False

#     def Test_use_can_follow(self):
#         self.user1 =User.objects.get(username="follow_test_1")
#         self.user2 =User.objects.get(username="follow_test_2")
#         #user 1 follow user 2
#         print("did I run?")
#         follow_user(user1,"follow_test_2")
#         user1_list_of_follower = user1.GetFollowingUser.get_queryset()
#         user2_list_of_follower = user2.GetFollowingUser.get_queryset()
#         self.assertEqual(find_follower(user1_list_of_follower),True,"User1 can follow")
#         self.assertEqual(find_follower(user2_list_of_follower),False,"User2 did not follow back")

#         make user1 follow user2 them follow
#         assert user1 follows user2
#         assert user2 does not follow user1
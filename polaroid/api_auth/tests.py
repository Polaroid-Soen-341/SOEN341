from django.test import TestCase
from ptest.ptest import PolaroidUserTest
from .models import User, UserManager
from .serializers import UserSerializer

class UserCreationTestCase(PolaroidUserTest):
    def setUp(self):
        self.create_default_test_user("uctc")

    def test_user_were_created(self):
        """Test that user was created"""
        owner = ...
        err_msg = ""
        try:
            owner = User.objects.get(username=self.username)
            owner.full_clean()
        except Exception as e:
            err_msg = str(e)
            owner = None
        #verify creation
        self.assertEqual(err_msg,"","Error: " + err_msg)
        self.assertIsNot(owner, None, "User \"" + self.username + "\" was not found")
        #Verify all fields match model
        self.assertEqual(owner.is_staff,False,"staff False")
        self.assertEqual(owner.is_superuser,False,"Super User False")
        self.assertEqual(owner.username,self.username,"username match")
        self.assertEqual(owner.email,self.email,"email match")
    
    def test_username_lenght(self):
        """test_user_name_length_limit"""
        user = ...
        try:
            toolong= 'x'*120
            user = self.create_default_test_user(username=toolong)
            user.full_clean()
        except:
            user = None
        self.assertEqual(user, None, "Error:user was created")
        #user should not be created
        
    def test_firstname_lenght(self):
        """test_user_first_name_limit"""
        user = ...
        try:
            toolong= 'x'*120
            user = self.create_default_test_user(username=self.username+"f", first_name=toolong)
            user.full_clean()
        except:
            user = None
        self.assertEqual(user, None, "Error:user was created")
        #user should not be created
        
    def test_lastname_lenght(self):
        """test_user_Last_name_limit"""
        user = ...
        try:
            toolong= 'x'*120
            user = self.create_default_test_user(username=self.username+"l", last_name=toolong)
            user.full_clean()
        except:
            user = None
        self.assertEqual(user, None, "Error:user was created")
        #user should not be created

class SuperUserCreationTestCase(PolaroidUserTest):
    
    def setUp(self):
        self.create_default_test_superuser("suctc")

    def test_user_were_created(self):
        """Test that SuperUser was created"""
        owner = ...
        err_msg = ""
        try:
            owner = User.objects.get(username=self.username)
            owner.full_clean()
        except Exception as e:
            err_msg = str(e)
            owner = None
        #Verify creation
        self.assertEqual(err_msg,"","Error: " + err_msg)
        self.assertIsNot(owner, None, "User \"" + self.username + "\" was not found")
        #Verify all fields match model
        self.assertEqual(owner.is_staff,True,"staff true")
        self.assertEqual(owner.is_superuser,True,"Super User true")
        self.assertEqual(owner.username,self.username,"username match")
        self.assertEqual(owner.email,self.email,"email match")
    
    def test_username_lenght(self):
        """test_Super_Username_length_limit"""
        user = ...
        try:
            toolong= 'x'*120
            user = self.create_default_test_user(username=toolong)
            user.full_clean()
        except:
            user = None
        self.assertEqual(user, None, "user was created")
        #user should not be created
        
    def test_firstname_lenght(self):
        """test_Super_first_name_length_limit"""
        user = ...
        try:
            toolong= 'x'*120
            user = self.create_default_test_user(username=self.username+"f", first_name=toolong)
            user.full_clean()
        except:
            user = None
        self.assertEqual(user, None, "user was created")
        #user should not be created
        
    def test_lastname_lenght(self):
        """test_Super_Last_name_length_limit"""
        user = ...
        try:
            toolong= 'x'*120
            user = self.create_default_test_user(username=self.username+"l", last_name=toolong)
            user.full_clean()
        except:
            user = None
        self.assertEqual(user, None, "user was created")
        #user should not be created

class UserModelsSerializerTestCase(PolaroidUserTest):
    def setUp(self):
        self.user1 = self.create_default_test_user("umstc1")
        self.user2 = self.create_default_test_user("umstc2")
    
    def test_following_users(self):
        """Testing follower serializer"""
        self.user1.following.add(self.user2)
        self.user1.save()
        self.assertEqual(self.user2 in self.user1.following.all(), True)
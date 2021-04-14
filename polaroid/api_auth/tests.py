from django.test import TestCase
from ptest.ptest import PolaroidUserTest
from .models import *

# Create your tests here.
class UserCreationTestCase(PolaroidUserTest):
    def setUp(self):
        self.create_default_test_user()

    def test_user_were_created(self):
        """Test that user was created"""
        owner = ...
        err_msg = ""
        try:
            owner = User.objects.get(username=self.username)
        except Exception as e:
            err_msg = str(e)
            owner = None
        
        self.assertEqual(err_msg,"","Error: " + err_msg)
        self.assertIsNot(owner, None, "User \"" + self.username + "\" was not found")
        self.assertEqual(owner.is_staff,False,"staff False")
        self.assertEqual(owner.is_superuser,False,"Super User False")
        self.assertEqual(owner.username,self.username,"username match")
        self.assertEqual(owner.email,self.email,"email match")

class SuperUserCreationTestCase(PolaroidUserTest):
    def setUp(self):
        self.create_default_test_superuser()

    def test_user_were_created(self):
        """Test that user was created"""
        owner = ...
        err_msg = ""
        try:
            owner = User.objects.get(username=self.username)
        except Exception as e:
            err_msg = str(e)
            owner = None
        
        self.assertEqual(err_msg,"","Error: " + err_msg)
        self.assertIsNot(owner, None, "User \"" + self.username + "\" was not found")
        self.assertEqual(owner.is_staff,True,"staff true")
        self.assertEqual(owner.is_superuser,True,"Super User true")
        self.assertEqual(owner.username,self.username,"username match")
        self.assertEqual(owner.email,self.email,"email match")

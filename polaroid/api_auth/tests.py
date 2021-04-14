from django.test import TestCase
from .models import *

# Create your tests here.
class UserCreationTestCase(TestCase):
    def setUp(self):
        User.objects.create_user("admin","admin@admin.com","stronpass")

    def test_user_were_created(self):
        """Test that user was created"""
        owner = User.objects.get(name)
        self.assertEqual(owner.is_staff,False,"staff False")
        self.assertEqual(owner.is_superuser,False,"Super User False")
        self.assertEqual(owner.username,"admin","username match")
        self.assertEqual(owner.email,"admin@admin.com","email match")
        self.assertEqual(owner.password,"strongpass","pass match")

class SuperUserCreationTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser("admin","admin@admin.com","stronpass")

    def test_user_were_created(self):
        """Test that user was created"""
        owner = User.objects.get(name)
        self.assertEqual(owner.is_staff,True,"staff true")
        self.assertEqual(owner.is_superuser,True,"Super User true")
        self.assertEqual(owner.username,"admin","username match")
        self.assertEqual(owner.email,"admin@admin.com","email match")
        self.assertEqual(owner.password,"strongpass","pass match")

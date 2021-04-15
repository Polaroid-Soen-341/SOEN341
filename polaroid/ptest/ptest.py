from django.test import TestCase
from api_auth.models import User

#add method to django TestCase to make email and password based on username
class PolaroidUserTest(TestCase):
    
    def __create_user(self, callback, username="", password="", first_name="", last_name="", is_superuser=False):
        self.username = username
        self.username = self.username.lower()
        self.email = self.username + "@tests.com"
        if password == "":
            self.password = self.username[-1:]
        else:
            self.password = password
        user = ...
        if is_superuser:
            user = callback(username=self.username,email=self.email, password=self.password)
        else:
            user = callback(username=self.username,email=self.email, password=self.password, first_name=first_name, last_name=last_name)
        return user

    def create_default_test_user(self, username, password=" ", first_name="", last_name=""):
        return self.__create_user(User.objects.create_user, username=username, password=password, first_name=first_name, last_name=last_name)

    def create_default_test_superuser(self, username, password=""):
        return self.__create_user(User.objects.create_superuser, username=username, password=password, is_superuser=True)

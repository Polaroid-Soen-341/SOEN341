from django.test import TestCase
from api_auth.models import User

class PolaroidUserTest(TestCase):
    def __create_user(self, callback, username):
        self.username = username
        self.username = self.username.lower()
        self.email = self.username + "@tests.com"
        self.password = self.username[-1:]
        callback(username=self.username,email=self.email, password=self.password)

    def create_default_test_user(self, username=""):
        if username == "":
            username = type(self).__name__
        self.__create_user(User.objects.create_user, username)

    def create_default_test_superuser(self):
        if username == "":
            username = type(self).__name__
        self.__create_user(User.objects.create_superuser, username)

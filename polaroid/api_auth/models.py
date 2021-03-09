from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

class PolaroidUserManager(BaseUserManager):

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(email=self.normalize_email(email),
                          username=username.lower(),
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class PolaroidUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    fullname = models.CharField(max_length=60, blank=True)
    bio = models.TextField(blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="user_followers",
                                    blank=True,
                                    symmetrical=False)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="user_following",
                                    blank=True,
                                    symmetrical=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = PolaroidUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def number_of_followers(self):
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    def number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    def __str__(self):
        return self.username


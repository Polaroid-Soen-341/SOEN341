from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

class UserManager(BaseUserManager):
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

    
    def create_superuser(self, username, email, password):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username            = models.CharField(max_length=20, unique=True)
    email               = models.EmailField(unique=True)
    firstName           = models.CharField(max_length=20)
    lastName            = models.CharField(max_length=20)
    birthday            = models.DateField(blank=True, null=True)

    following           = models.ManyToManyField(
                            'self',
                            related_name="user_following",
                            null=True,
                            blank=True,
                            symmetrical=False
                        )
    
    is_active           = models.BooleanField(default=True)
    is_staff            = models.BooleanField(default=False)
    date_joined         = models.DateTimeField(auto_now_add=True)

    objects             = UserManager()

    USERNAME_FIELD      = 'username'
    REQUIRED_FIELDS     = ['email', 'password']

    def __str__(self):
        return self.username
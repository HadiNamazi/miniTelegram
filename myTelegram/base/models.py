from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Your implementation to create a user
        pass

    def create_superuser(self, email, password=None, **extra_fields):
        # Your implementation to create a superuser
        pass

    def get_by_natural_key(self, username):
        # Your implementation to retrieve a user by natural key
        # For example: return self.get(email=username)
        pass

class User(AbstractBaseUser):#TODO: hashing password
    username = models.CharField(max_length=20, blank=False, null=False)
    userId = models.CharField(max_length=10, blank=False, null=False, unique=True)
    contacts = models.TextField(max_length=100000, blank=True, null=True)

    REQUIRED_FIELDS = ['password', 'username']
    USERNAME_FIELD = 'userId'

    objects = UserManager()

    def __str__(self):
        return self.username

class Message(models.Model):
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromUser')
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toUser')
    text = models.TextField(max_length=500, blank=False, null=False)
    datetime = models.DateTimeField(auto_now_add=True)
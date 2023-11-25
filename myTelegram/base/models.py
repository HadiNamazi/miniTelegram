from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    username = models.CharField(max_length=20, blank=False, null=False)
    userId = models.CharField(max_length=10, blank=False, null=False, unique=True)
    contacts = models.ManyToManyField('self')

    REQUIRED_FIELDS = ['password', 'username']
    USERNAME_FIELD = 'userId'

    def __str__(self):
        return self.username

class Message(models.Model):
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromUser')
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toUser')
    text = models.TextField(max_length=500, blank=False, null=False)
    datetime = models.DateTimeField(auto_now_add=True)
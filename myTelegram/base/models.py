from django.db import models
from django.contrib.auth.models import User as DefaultUser

class User(DefaultUser):
    name = models.CharField(max_length=20, blank=True, null=True)
    contacts = models.ManyToManyField('self')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password', 'name']

class Message(models.Model):
    fromUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromUser')
    toUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='toUser')
    text = models.TextField(max_length=500, blank=False, null=False)
    datetime = models.DateTimeField(auto_now_add=True)
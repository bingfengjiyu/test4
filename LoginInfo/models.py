from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=128)
    phone=models.CharField(max_length=128)
    email=models.CharField(max_length=128, default=None)
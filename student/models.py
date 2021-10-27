from django.db import models
from django.contrib.auth.models import AbstractUser
from leadership.models import User
from django.db.models.deletion import CASCADE
# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
    username=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True)
    

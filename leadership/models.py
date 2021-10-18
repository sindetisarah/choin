from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser,User
import uuid
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
# Create your models here.
class User(AbstractUser):
    user_name = models.CharField(('username'), unique=True,max_length=40),
    email = models.EmailField(('email address'), unique=True)
    password=models.CharField(('password'),max_length=100,default=uuid.uuid4)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

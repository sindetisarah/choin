from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
import uuid
from django.db.models.fields import CharField
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    # password=models.CharField(('password'),max_length=100,default=uuid.uuid4)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
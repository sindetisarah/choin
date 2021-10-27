from django.db import models
from django.db.models.deletion import CASCADE
from leadership.models import User
# Create your models here.

class Trainer(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
    username=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True)
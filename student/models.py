from django.db import models
from django.contrib.auth.models import AbstractUser
from leadership.models import User
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True,related_name='userprofile')
    image = models.ImageField(upload_to='profile_image', blank=True)
    gender = models.CharField(default='', blank=True, max_length=20)
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role==3:
            Student.objects.create(user=instance)
    else:
        pass
   

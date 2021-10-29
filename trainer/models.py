from django.db import models
from django.db.models.deletion import CASCADE
from leadership.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
# Create your models here.
# @receiver(post_save, sender=User)
class Trainer(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True)
#     username=models.CharField(max_length=50,null=True)
#     email=models.EmailField(null=True)
    

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

     #add this
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
# 	if created:
# 		User.objects.get_or_create(user=instance)
        # user.save()

# @receiver(post_save, sender=User) #add this
# def save_user_profile(sender, instance, **kwargs):
    
    
# 	instance.profile.save()

# class Trainer(User):
#     user=models.OneToOneField(User,on_delete=CASCADE,related_name='profile')
    
from django.db import models
from django.db.models.deletion import CASCADE
from leadership.models import User , Wallet
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Trainer(models.Model):
    user=models.OneToOneField(User,on_delete=CASCADE,null=True,related_name='traineruserprofile')
    image = models.ImageField(upload_to='profile_image', blank=True)
    gender = models.CharField(default='', blank=True, max_length=20)
    
# trainer=User.objects.all().filter(role=2)    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role==2:
            Trainer.objects.create(user=instance)
            # Wallet.objects.create(owner=instance)
    else:
        pass
    

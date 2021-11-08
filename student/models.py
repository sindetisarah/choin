from django.db import models
from django.contrib.auth.models import AbstractUser
from leadership.models import User , Wallet
from django.db.models.deletion import CASCADE, SET_NULL
from django.dispatch import receiver
from django.db.models.signals import post_save
from leadership.models import RedeemableItem
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
            Wallet.objects.create(owner=instance)
    else:
        pass

class Order(models.Model):
	product = models.ForeignKey(RedeemableItem,on_delete=models.CASCADE)
	customer = models.ForeignKey(Student,on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	price = models.IntegerField()
	phone = models.CharField(max_length=15,blank=True)
	completed = models.BooleanField(default=False)


	def __str__(self):
		return self.customer.email
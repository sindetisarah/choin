from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser,User
import uuid

# Create your models here.
class User(AbstractUser):
    user_name = models.CharField(('username'), unique=True,max_length=40),
    email = models.EmailField(('email address'), unique=True)
    is_superadmin = models.BooleanField(('is_superadmin'), default=False)
    is_active = models.BooleanField(('is_active'), default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def __str__(self):
        """stirng representation"""
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

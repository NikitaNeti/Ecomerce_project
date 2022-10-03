from django.db import models

# Create your models here.
from django.contrib.auth.models import(AbstractUser)
from enum import Enum
from .manager import *
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.


class status(Enum):
    active = "1"
    inactive = "0"

class Reg_method(Enum):   
    Normal = 'N'
    Facebook = 'F'
    Twitter ='T'
    Google ='G'

class User(AbstractUser):
    
    username = None
    email = models.EmailField(max_length=45,unique=True)
    password=models.CharField(max_length=255)
    status = models.CharField(max_length=12, choices=[(tag, tag.value) for tag in status])
    created_date = models.DateField(auto_now=True)
    fb_token = models.CharField(max_length=100)
    twitter_token = models.CharField(max_length=100)
    google_token = models.CharField(max_length=100)
    # registration_method = models.CharField(Reg_method,default=Reg_method.Normal) 
    registration_method = models.CharField(max_length=12, choices=[(x, x.value) for x in Reg_method])

    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


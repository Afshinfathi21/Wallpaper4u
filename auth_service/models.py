from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField( max_length=254,unique=True)
    profile_img=models.ImageField(upload_to='users/%Y%m%d',blank=True,default='src/default_user.png')
    bio = models.TextField()

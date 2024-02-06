from statistics import mode
from django.db import models
from auth_service.models import CustomUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name



class Post(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_img=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    placeholder=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)

    def get_like_count(self):
        return self.likes.count()


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='likes',on_delete=models.CASCADE)
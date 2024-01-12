from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title= models.CharField(max_length=255)
    content = models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE,default=12345)
    date=models.DateField(auto_now_add=True)
    featured = models.BooleanField(default=False)

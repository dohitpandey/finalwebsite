from django.db import models
from autoslug import AutoSlugField

class user(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    profile_pic=models.FileField(upload_to="picture/", default="/dp.png")
    nameslug=AutoSlugField(populate_from='name', unique=True, null=True, default=None)

class friends(models.Model):
    lou=models.OneToOneField(user,on_delete=models.CASCADE,related_name="list_of_users")
    lof=models.ManyToManyField(user,related_name="list_of_friends")
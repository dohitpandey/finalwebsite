from django.db import models

class user(models.Model):
    name=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    profile_pic=models.FileField(upload_to="picture", max_length=250, null=True, default=None)
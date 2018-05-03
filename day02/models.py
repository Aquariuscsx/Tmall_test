from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    head = models.FileField(upload_to='upload/user')


from django.db import models

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)

    # class Meta:
    #     db_table = 't_user'

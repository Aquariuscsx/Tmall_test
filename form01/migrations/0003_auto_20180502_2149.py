# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form01', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=32),
        ),
    ]

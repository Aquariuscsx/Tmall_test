# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-02 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]

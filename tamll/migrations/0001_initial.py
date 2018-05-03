# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-26 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'T_SHOP_CAR',
            },
        ),
        migrations.CreateModel(
            name='ShopDetail',
            fields=[
                ('detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('detail_content', models.TextField()),
            ],
            options={
                'db_table': 'T_Shop_Detail',
            },
        ),
        migrations.CreateModel(
            name='ShopInfo',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=64)),
                ('shop_title', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'db_table': 'T_Shop_Info',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'T_USER',
            },
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['username'], name='T_USER_usernam_06bd13_idx'),
        ),
        migrations.AddIndex(
            model_name='shopinfo',
            index=models.Index(fields=['shop_name', 'shop_title'], name='T_Shop_Info_shop_na_52fedd_idx'),
        ),
        migrations.AddField(
            model_name='shopdetail',
            name='shop_info',
            field=models.OneToOneField(db_column='shop-id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='tamll.ShopInfo'),
        ),
        migrations.AddField(
            model_name='shopcar',
            name='shop_info',
            field=models.ForeignKey(db_column='shop_id', on_delete=django.db.models.deletion.CASCADE, to='tamll.ShopInfo'),
        ),
        migrations.AddIndex(
            model_name='shopcar',
            index=models.Index(fields=['shop_info'], name='T_SHOP_CAR_shop_id_02fab2_idx'),
        ),
    ]
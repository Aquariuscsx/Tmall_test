from django.db import models


class Address(models.Model):
    aid = models.AutoField(primary_key=True)
    take_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=32)
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=11)

    class Meta:
        db_table = 'Address'


class ShowProduct(models.Model):
    sid = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=64)
    shop_title = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=8, decimal_places=3)
    promotion_price = models.DecimalField(max_digits=8, decimal_places=3)
    sales_volume = models.IntegerField()
    count = models.IntegerField()
    stock = models.IntegerField()

    class Meta:
        db_table = 'Show_Product'


class ShopXq(models.Model):
    xid = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=64)
    brand = models.CharField(max_length=64)
    sid = models.OneToOneField(ShowProduct, on_delete=models.SET_NULL, db_column='sid', to_field='sid', null=True)

    class Meta:
        db_table = 'Shop_XQ'


class ShopUser(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = 'Shop_user'


class ShopCar(models.Model):
    car_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sid = models.ForeignKey(ShowProduct, on_delete=models.CASCADE, db_column='sid', to_field='sid')
    uid = models.ForeignKey(ShopUser, on_delete=models.CASCADE, db_column='uid', to_field='uid')

    class Meta:
        db_table = 'Shop_car'

from django.db import models


# Create your models here.


class Tmal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    subtitle = models.CharField(max_length=255, default='都是好东西')
    orignalprice = models.DecimalField(max_digits=8, decimal_places=2, default='1')
    promoteprice = models.DecimalField(max_digits=8, decimal_places=2, default='1')
    stock = models.IntegerField(default=0)
    create_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Tmall'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'T_USER'
        indexes = [
            models.Index(fields=['username']),
        ]


# 一对一的关系
# 主表 从表(设置外键)
# 第一个作用 夺标查询需要取笛卡尔积
# 通过主表查询从表的信息
class ShopInfo(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=64)
    shop_title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        db_table = 'T_Shop_Info'
        indexes = [
            models.Index(fields=['shop_name', 'shop_title']),
        ]


class ShopDetail(models.Model):
    detail_id = models.AutoField(primary_key=True)
    # detail_content = models.CharField(max_length=255)
    detail_content = models.TextField()
    '''
    to : 要关联的对象  (关联的表)
    on_delete = 可选值
                models.CASCADE 级联删除
                models.SET_NULL  外键设置null
                DO_NOTHING  什么都不做
                PROTECT  删除数据会引发错误
                models.SET
                
    to_field  参照的字段  默认是主键 
    外键再书记库里的命名  默认是 表名_主键的名字
    '''

    # 外键的要求  参照的列必须唯一
    # 默认
    shop_info = models.OneToOneField(ShopInfo, on_delete=models.SET_NULL, db_column='shop_id', to_field='shop_id',
                                     null=True)

    class Meta:
        db_table = 'T_Shop_Detail'


class ShopCar(models.Model):
    car_id = models.AutoField(primary_key=True)
    count = models.IntegerField(default=0)
    # 实现一对多的关系
    shop_info = models.ForeignKey(ShopInfo, on_delete=models.CASCADE, db_column='shop_id', to_field='shop_id')

    class Meta:
        db_table = 'T_SHOP_CAR'

        indexes = [
            models.Index(fields=['shop_info']),
        ]

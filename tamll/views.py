import hashlib

from django.shortcuts import render

# Create your views here.
# from tamll.models import Tmal
#
#
# def add_mall(request):
#     name = '老王'
#     content = {'name': name}
#     user = Tmal.objects.filter()
#     return render(request, 'temp01.html', content)
#
#
# def test(request):
#     # selece * from Tmal
#     # users = Tmal.objects.all()
#     # for user in users:
#     #     print(user)
#     # 相当于 select * from Tmal where uaername = 'xiaoming'
#     # good_list = Tmal.objects.filter(username='xiaoming')
#
#     # 反向查询
#     users = Tmal.objects.exclude(username = 'xiaoming')
#
#
#     return render(request, 'temp01.html')
from tamll.models import User, ShopCar, ShopInfo, ShopDetail


def add_shop_car(request):
    user = User()
    user.username = 'zhangsuo'
    # user.password = '123'
    user.password = hashlib.md5('123'.encode('utf-8')).hexdigest()
    user.save()
    # shop_items = []
    # for i in range(10):
    #     sc = ShopCar(count=i,username=user.username, shop_info_id=1)
    #     shop_items.append(sc)
    # ShopCar.objects.bulk_create(shop_items)
    return render(request, 'index.html')


# 查询 所有的购物车信息
def find_shop_items(request):
    uid = request.GET.get('user_id')
    ShopCar.objects.filter(user_id=uid)
    users = User.objects.all()
    for user in users:
        shop_items = ShopCar.objects.filter(user_id=user.user_id)
        # 讲用户下的所有的购物车信息保存到对象中
        user.shop_items = shop_items

    print(users)
    # 前端  + 模板语言
    content = {'users': users}
    return render(request, 'index.html')


class Test:
    def __init__(self):
        self.age = 18
        self.name = 'xm'


def test_templates(request):
    li = [1, 2, 3, 4, 5]
    dic = {
        'name': '131231',
        'pwd': '123,'
    }
    content = {
        'num': 1,
        'li': li,
        'dic': dic,
        'test': Test(),
    }
    return render(request, 'home/temp01.html',content)

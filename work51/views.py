from django.http import HttpResponse
from django.shortcuts import render

from work51.models import Address, ShopUser, ShowProduct


def take_address(request):
    if request.method == 'GET':
        address = request.GET.get('take_address')
        postal_code = request.GET.get('postal_code')
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        take = Address()
        take.take_address = address
        take.postal_code = postal_code
        take.name = name
        take.phone = phone
        take.save()
    return render(request, 'home/work51.html')


def login(request):
    if request.method == 'POST':
        login_name = request.POST.get('login_name')
        password = request.POST.get('login_password')
        conf_password = request.POST.get('conf_password')
        user = ShopUser()
        user.username = login_name
        user.password = password
        user.conf_password = conf_password
        if conf_password == password:
            user.save()
            return HttpResponse('注册成功')
        else:
            return HttpResponse('两次密码不同')


def add(request):
    product = ShowProduct(shop_name='夏普', shop_title='32寸 液晶显示屏', original_price=2000, promotion_price=1600,
                          sales_volume=1500, count=1, stock=10000)
    ShowProduct.objects.bulk_create(product)
    return render(request, 'index.html')

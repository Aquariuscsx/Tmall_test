from django.conf.urls import url, include
from django.contrib import admin

from tamll import views

urlpatterns = [
    url('admin/', admin.site.urls),
    # url('add_mall/', views.add_mall),
    # url('test/', views.test),
    url('find_shop_items/', views.find_shop_items),
    url('add_shop_car/', views.add_shop_car),
    url('test/', views.test_templates),
    url('day02/', include('day02.urls')),
    url('work51/', include('work51.urls')),
    url('form01/', include('form01.urls')),
    url('cookie/', include('cookie.urls')),
    # url('^$', views.index),
]

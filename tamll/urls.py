from django.conf.urls import url

from tamll import views

urlpatterns = [
    url('find_shop_items/', views.find_shop_items),
    url('add_shop_car/', views.add_shop_car),
    url('test/', views.test_templates),



]
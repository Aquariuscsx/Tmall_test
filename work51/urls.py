from django.conf.urls import url

from work51 import views

urlpatterns = [
    url('work51/', views.take_address),
    url('login/', views.login),
    url('add/', views.add),

]
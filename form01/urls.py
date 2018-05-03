from django.conf.urls import url

from form01 import views

urlpatterns = [
    # views.对象.as_view()
    url('test01/', views.test),
    url('register01/', views.register)

]

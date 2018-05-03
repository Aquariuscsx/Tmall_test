from django.conf.urls import url

from cookie import views

urlpatterns = [
    # views.对象.as_view()
    url('cookie/', views.test_cookie),
    url('cookie02/', views.test_cookie2),
    url('session/', views.test_session),
    url('session02/', views.test_session2),

]

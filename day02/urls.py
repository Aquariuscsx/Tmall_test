from django.conf.urls import url

from day02 import views

urlpatterns = [
    # views.对象.as_view()
    url(r'^upload/', views.UploadFile.as_view),
    url('^day02/', views.upload),
    url(r'^register/', views.upload1),

]
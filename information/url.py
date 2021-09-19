from django.conf.urls import url
from information import views

urlpatterns = [
    url('^postinformation/', views.postinformation),
    url('^viewinformation/', views.viewinformation),

]

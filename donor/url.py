from django.conf.urls import url
from donor import views


urlpatterns = [
    url('^registerdonor/', views.registertdonor),
   # url('^viewdonor/', views.viewdonor),

]

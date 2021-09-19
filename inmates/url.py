from django.conf.urls import url
from inmates import views

urlpatterns = [
    url('^register/', views.register),


]

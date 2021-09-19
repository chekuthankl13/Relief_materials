from django.conf.urls import url
from camp import views


urlpatterns = [
    url('^managecamp/', views.managecamp),
    url('^registercamp/', views.registercamp),
    url('^viewcamp/', views.viewcamp),
    url('^approve/(?P<idd>\w+)',views.approve,name='approve'),
    url('^reject/(?P<idd>\w+)',views.reject,name='reject'),
]

from django.conf.urls import url
from authority import views


urlpatterns = [
    url('^manageauthority/', views.manageauthority ),
    url('^registerauthority/', views.registerauthority),
    url('^sapprove/(?P<idd>\w+)',views.approve,name='sapprove'),
    url('^sreject/(?P<icc>\w+)',views.reject,name='sreject'),
]

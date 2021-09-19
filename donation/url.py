from django.conf.urls import url
from donation import views


urlpatterns = [
    #url('^managedonation/', views.managedonation),
    url('^viewdonation/', views.viewdonation),
    url('^forward/(?P<idd>\w+)', views.forward, name='forward'),
    url('^viewdonationbyauthority/', views.vdauthority),
    url('^allocate/(?P<icc>\w+)', views.acamp, name='allocate'),

]

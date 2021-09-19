from django.conf.urls import url
from camp_requirement import views


urlpatterns = [
    url('^requestcamprequirement/', views.requestcamprequirement),
    url('^viewcamprequirement/', views.viewcamprequirement),
    url('^managecamprequirement/', views.managecamprequest),
    url('^capprove/(?P<idd>\w+)',views.capprove,name='capprove'),
    url('^creject/(?P<idd>\w+)',views.creject,name='creject'),

]

from django.conf.urls import url
from donation_request import views


urlpatterns=[
    url('^managedonationrequest/', views.managedonationrequest),
    url('^requestdonationrequest/', views.requestdonationrequest),
    url('^viewdonationrequest/', views.viewdonationrequest),
    url('^viewstatusdonationrequest/', views.viewstatusdonationrequest),
    url('^viewdonationrequestbydonor/', views.viewdonationrequestbydonor),
    url('^dapprove/(?P<idd>\w+)', views.approve, name='dapprove'),
    url('^dreject/(?P<icc>\w+)', views.reject, name='dreject'),
    url('^forward/(?P<iff>\w+)', views.donorforward, name='forward'),
    #######-----my work---------########
     url('^doapprove/(?P<doidd>\w+)', views.doapprove, name='doapprove'),
     url('^doreject/(?P<doicc>\w+)', views.doreject, name='doreject'),
]

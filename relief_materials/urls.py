"""relief_materials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [


    path('admin/', admin.site.urls),
    url('^allocateinmates/', include('allocate_inmates.url')),
    url('^authority/', include('authority.url')),
    url('^awareness/', include('awareness.url')),
    url('^camp/', include('camp.url')),
    #url('^camprequest/', include('camp_request.url')),
    url('^camprequirement/', include('camp_requirement.url')),
    url('^donation/', include('donation.url')),
    url('^donationrequest/', include('donation_request.url')),
    url('^donor/', include('donor.url')),
    url('^information/', include('information.url')),
    url('^inmates/', include('inmates.url')),
    url('^login/', include('login.url')),


]

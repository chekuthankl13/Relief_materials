from django.conf.urls import url
from allocate_inmates import views
urlpatterns = [
    url('^allocate/',views.allocatedonation),
]

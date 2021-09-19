from django.conf.urls import url
from awareness import views


urlpatterns = [
    url('^postawareness/', views.postawareness ),
    url('^viewawareness/', views.viewawareness),
]

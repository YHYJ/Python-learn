from django.conf.urls import url
from . import views

app_name = 'booktest'


urlpatterns = [
    url(r'^session_set/$', views.session_set, name='session_set'),
    url(r'^session_get/$', views.session_get, name='session_get'),
]

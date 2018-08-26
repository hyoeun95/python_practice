from django.conf.urls import url
from . import views


urlpatterns = [
    # post views
    url(r'^$', views.login, name='index'),
    url(r'login/^$', views.login, name='list'),
    #url(r'^login/$', views.login, name='login'),
]

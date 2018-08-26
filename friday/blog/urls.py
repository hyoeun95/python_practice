from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', PostLV.as_view(), name="index"),         #post_list.html 보여
    url(r'^post/^$', PostLV.as_view(), name="list"),     #선언 해 주어야 아래 문장 실행 가능
    url(r'^post/(?P<slug>[-\w]+)/$', post_dtail, name="detail"),    #어떤 슬러그 값으로 이동할 지 지정
]
from django.conf.urls import url, include
from fighter.views import *

urlpatterns = [
    # url(r'^$', index),
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^lesson_one/$', lesson_one),
    url(r'^lesson_two/$', lesson_two),
    url(r'^tmp/$', tmp),
    url(r'myadmin/$', myadmin),
    url(r'^tmp_two/$', tmp_two),
]

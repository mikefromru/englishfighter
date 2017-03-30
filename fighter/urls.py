from django.conf.urls import url, include
from fighter.views import *

urlpatterns = [
    # url(r'^$', index),
    url(r'^$', demo),
    url(r'^demo/$', demo),
]

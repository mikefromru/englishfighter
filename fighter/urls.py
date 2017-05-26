from django.conf.urls import url, include
from fighter.views import *

urlpatterns = [
    # url(r'^$', index),
    url(r'^$', demo),
    url(r'^demo/$', demo),
    url(r'^lesson_one', lesson_one),
    url(r'^lesson_two', lesson_two),
    url(r'^tmp/$', tmp),
]

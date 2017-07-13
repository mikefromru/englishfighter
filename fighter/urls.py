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
    url(r'^addition/$', addition),
    url(r'^data_edit/(?P<pk>[0-9]+)/edit/$', data_edit, name="data_edit"),
    url(r'^listdata/$', listdata, name="listdata"),
]

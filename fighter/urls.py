from django.conf.urls import url, include
from fighter.views import *

# from django.contrib.auth.views import login, logout

urlpatterns = [
    # url(r'^$', index),
    url(r'^$', demo),
    url(r'^demo/$', demo),
    
    # url(r'^login/$', LoginFormView.as_view()),
    url(r'^login/$', login),
    # url(r'^register/$', RegisterFormView.as_view()),
    url(r'^register/$', register),

    url(r'^logout/$', logout),
    url(r'^profile/$', profile),
    url(r'^tmp/$', tmp),
    # url('', include('django.contrib.auth.urls', namespace='auth')),
]

from django.conf.urls import url
from .views import *

urlpatterns = [
    # url(r'^$', index),
    # url(r'^$', demo),
    # url(r'^demo/$', demo),
    
    # url(r'^login/$', LoginFormView.as_view()),
    url(r'^login/$', login),
    # url(r'^register/$', RegisterFormView.as_view()),
    url(r'^register/$', register),

    url(r'^logout/$', logout),
    url(r'^profile/$', profile),
    url(r'^tmp/$', tmp),
]
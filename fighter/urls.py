from django.conf.urls import url
from fighter.views import *

# from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^demo/$', demo),
    
    url(r'^login/$', LoginFormView.as_view()),
    url(r'^register/$', RegisterFormView.as_view()),

    url(r'^logout/$', LogoutView.as_view()),
    url(r'^profile/$', profile),
    url(r'^tmp/$', tmp),
]

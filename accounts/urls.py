from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^profile/$', profile),
    url(r'^editing/$', editing_profile),
]

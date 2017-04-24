"""englishfighter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('fighter.urls')),
    url(r'^fighter/', include('fighter.urls')),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
    name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url('', include('social_django.urls', namespace='social')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
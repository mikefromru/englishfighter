from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.template import TemplateDoesNotExist
from django.http import Http404

from django.contrib import auth

# for Registration
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

# for Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

# for Logout
from django.views.generic.base import View
from django.contrib.auth import logout 

class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'fighter/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    # template_name = "fighter/login.html"
    template_name = 'fighter/register.html'
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/index")

def index(request):
    try:
        if request.POST.get('login'):
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/demo')
            else:
                # return HttpResponse('you are a fuckin bitch')
                # return HttpResponseRedirect('/login')
                pass

        return render(request, "fighter/index.html")
    except TemplateDoesNotExist:
        raise Http404() 

def demo(request):
    return render(request, 'fighter/demo.html')

def profile(request):
    if request.user.is_authenticated():
        return render(request, 'fighter/profile.html')
    else:
        return render(request, 'fighter/login.html')


def tmp(request):
    return render(request, 'fighter/tmp.html')
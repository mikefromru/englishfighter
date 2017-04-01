from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response
# from django.template import TemplateDoesNotExist
# from django.http import Http404

# from django.contrib import auth

# # for Registration
# from django.views.generic.edit import FormView
# from django.contrib.auth.forms import UserCreationForm

# # for Authentication
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import auth

# # for Logout
# from django.views.generic.base import View

# # from .forms import RegistrationForm

# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # user.set_password()
#             user = auth.authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1'))
#             auth.login(request, user)
#             return HttpResponseRedirect('/profile')
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/register.html', {'form': form})       


# def login(request):
#     form = {}
#     if request.POST:
#         username = request.POST.get('username', '')
#         password = request.POST.get('password', '')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None and user.is_active:
#             auth.login(request, user)
#             return HttpResponseRedirect('/demo')
#         else:
#             form['login_error'] = 'Неправильный логин или пароль'
#             return render(request, 'accounts/login.html', form)
#     else:
#         return render(request, 'accounts/login.html', form)


# def logout(request):
#         auth.logout(request)
#         return HttpResponseRedirect("/demo")



def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')

    return render(request, 'accounts/profile.html')
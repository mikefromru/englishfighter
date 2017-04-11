from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.db import transaction

from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from .models import UserProfile


def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/profile.html')

@login_required
# @transaction.atomic
def editing_profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    user = request.user
    if request.method == "POST":
        userform = UserForm(request.POST, instance=user)
        profileform = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return redirect('/accounts/profile')
    else:
        userform = UserForm(instance=user)
        profileform = ProfileForm(instance=user.userprofile)

    return render(request, 'accounts/editing_profile.html', {
        'userform': userform,
        'profileform': profileform
        })
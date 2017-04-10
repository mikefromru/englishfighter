from django.shortcuts import render, HttpResponseRedirect, HttpResponse, render_to_response

def profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/profile.html')

def editing_profile(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login')
    return render(request, 'accounts/editing_profile.html')
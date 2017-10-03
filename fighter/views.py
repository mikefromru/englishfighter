# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from accounts.models import UserProfile
from fighter.models import (
    LessonOne, LessonTwo, LessonThree, LessonFour, LessonFive
)
from .forms import (
    LessonOneForm, LessonTwoForm, LessonThreeForm, LessonFourForm,
    LessonFiveForm
)

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# from django.views.decorators.csrf import csrf_exempt

def index(request):
    if request.user.is_authenticated():
        profile = UserProfile.objects.get(user=request.user)
        if profile.points == 400 or profile.points == 800:
            profile.pointsProgressBar = 0
            profile.save()
        # return render(request, 'fighter/index.html', {'profile_points': profile.points})
        # profile.pointsProgressBar = 50
        return render(request, 'fighter/index.html', {
                    'points_user': profile.points,
                    'profile_pointsProgressBar': profile.pointsProgressBar
                    })
    return render(request, 'fighter/index.html')

def myadmin(request):
    """Enter is only SUPERUSER"""
    if request.user.is_superuser:
        return render(request, 'fighter/myadmin.html')
    return HttpResponseNotFound("<h1>Page not found</h1>")

def addition(request):
    if not request.user.is_superuser:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
    if request.method == "POST":
        form = LessonFiveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addition')
    else:
        form = LessonFiveForm
    return render(request, 'fighter/addition.html', {'form': form})

def data_edit(request, pk):
    if not request.user.is_superuser:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    amount = LessonFive.objects.all()
    # some = get_object_or_404(LessonOne, pk=pk)
    some = get_object_or_404(LessonFive, pk=pk)

    if request.POST.get('delete'):
        some.delete()
        return HttpResponseRedirect("/listdata")
    if request.POST.get('save'):
        form = LessonFiveForm(request.POST, instance=some)
        if form.is_valid():
            form.save()
            return redirect('/listdata', pk=some.pk)
    else:
        form = LessonFiveForm(instance=some)
    return render(request, 'fighter/data_edit.html', {
        'form': form, 'amount': amount})

def listdata(request):
    if not request.user.is_superuser:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    # data = LessonOne.objects.order_by("-id")
    data = LessonFive.objects.order_by("-id")
    return render(request, 'fighter/listdata.html', {
        'data': data, 'amount': len(data)})

################### Name Lessons ############################

# @csrf_exempt
def lesson_one(request):
    ''' To be '''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    message = "Базовая форма глагола"
    stack = LessonOne.objects.order_by('?')[0]
    # stack = LessonTwo.objects.order_by()[88]
    # stack = LessonOne.objects.all().last()
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        if profile.points >= 400:
            pass
        else:
            profile.points += 2
        if profile.points >= 400:
            pass
        else:
            profile.pointsProgressBar += 1
        profile.save()
        return HttpResponseRedirect("/lesson_one")
    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})

def lesson_two(request):
    ''' Past simple, Present simple, Future simple '''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    message = 'Past simple Present simple Future simple'
    stack = LessonTwo.objects.order_by('?')[0]
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        if profile.points >= 800:
            pass
        else:
            profile.points += 2
        if profile.points >= 800:
            pass
        else:
            profile.pointsProgressBar += 1
        profile.save()
        return HttpResponseRedirect("/lesson_two")
    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})

def lesson_three(request):
    ''' Past continuous  Present continuous Future continuous '''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    message = 'Past continuous, Present continuous, Future continuous' 
    stack = LessonThree.objects.order_by('?')[0]
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        profile.points += 2
        profile.pointsProgressBar += 1
        profile.save()
        return HttpResponseRedirect("/lesson_three")
    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})

def lesson_four(request):
    ''' Present perfect '''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    message = 'Present perfect' 
    stack = LessonFour.objects.all().last()
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        profile.points += 2
        profile.pointsProgressBar += 1
        profile.save()
        return HttpResponseRedirect("/lesson_four")
    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})

def lesson_five(request):
    ''' Some-any, much-many, few-little  '''
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    message = 'Some-any, much-many, few-little' 
    # stack = LessonFour.objects.order_by('?')[0]
    # stack = LessonThree.objects.order_by()[77]
    stack = LessonFive.objects.all().last()
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        profile.points += 2
        profile.pointsProgressBar += 1
        profile.save()
        return HttpResponseRedirect("/lesson_five")
    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})

################# This is end of name ################

def tmp(request):
    return render(request, 'fighter/tmp.html')
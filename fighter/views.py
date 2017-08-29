# -*- coding: UTF-8 -*-
from django.shortcuts import render, HttpResponseRedirect, render_to_response, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from accounts.models import UserProfile
from fighter.models import LessonOne, LessonTwo, LessonThree
from .forms import LessonOneForm, LessonTwoForm, LessonThreeForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'fighter/index.html')

def myadmin(request):
    """Enter is only SUPERUSER"""
    if request.user.is_superuser:
        return render(request, 'fighter/myadmin.html')
    return HttpResponseNotFound("<h1>Page not found</h1>")

def addition(request):
    if not request.user.is_superuser:
        return HttpResponseNotFound("<h1>Page not found</h1>")
    
    # amount = LessonOne.objects.all()
    amount = LessonTwo.objects.all()
    if request.method == "POST":
        # form = LessonOneForm(request.POST)
        form = LessonTwoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addition')
    else:
        # form = LessonOneForm
        form = LessonTwoForm
    return render(request, 'fighter/addition.html', {'form': form,
    'amount': len(amount)})

def data_edit(request, pk):
    if not request.user.is_superuser:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    # amount = LessonOne.objects.all()
    amount = LessonTwo.objects.all()
    # some = get_object_or_404(LessonOne, pk=pk)
    some = get_object_or_404(LessonTwo, pk=pk)

    if request.POST.get('delete'):
        some.delete()
        return HttpResponseRedirect("/listdata")
    if request.POST.get('save'):
        # form = LessonOneForm(request.POST, instance=some)
        form = LessonTwoForm(request.POST, instance=some)
        if form.is_valid():
            form.save()
            return redirect('/listdata', pk=some.pk)
    else:
        # form = LessonOneForm(instance=some)
        form = LessonTwoForm(instance=some)
    return render(request, 'fighter/data_edit.html', {'form': form, 'amount': amount})

def listdata(request):
    if not request.user.is_superuser:
        return HttpResponseNotFound("<h1>Page not found</h1>")

    # data = LessonOne.objects.order_by("-id")
    data = LessonTwo.objects.order_by("-id")
    return render(request, 'fighter/listdata.html', {'data': data, 'amount': len(data)})


################### Name Lessons ############################

# @csrf_exempt
def lesson_one(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    message = "Базовая форма глагола"
    stack = LessonOne.objects.order_by('?')[0]
    # stack = LessonOne.objects.all().last()

    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        profile.points += 2
        profile.save()
        return HttpResponseRedirect("/lesson_one")
        print("hello++++++++++++++")

    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})

def lesson_two(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')

    message = 'Местоимения. Вопросительные слова'
    # stack = LessonTwo.objects.order_by('?')[0]
    # stack = LessonTwo.objects.order_by()[88]
    stack = LessonTwo.objects.all().last()
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        profile.points += 2
        profile.save()
        return HttpResponseRedirect("/lesson_two")
    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})


################# This is end of name ################


def tmp(request):
    message = "The lesson TMP"
    stack = LessonOne.objects.order_by('?')[0]

    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        profile.points += 2
        profile.save()
        return HttpResponseRedirect("/tmp")
        print("hello++++++++++++++")

    return render(request, 'fighter/tmp.html', {
        'stack': stack,
        'message': message})

def tmp_two(request):
    return render(request, 'fighter/tmp_two.html')
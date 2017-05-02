from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.contrib.auth.models import User
from accounts.models import UserProfile
from fighter.models import LessonOne 

import platform

# from django.views.decorators.csrf import csrf_exempt

def demo(request):
    return render(request, 'fighter/demo.html')

# @csrf_exempt
def lesson_one(request):
    message = "The lesson number 1"
    stack = LessonOne.objects.order_by('?')[0]

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
    message = 'The lesson number 2'
    stack = LessonOne.objects.order_by('?')[0]
    if request.method == "POST":
        profile = UserProfile.objects.get(user=request.user)
        profile.points += 2
        profile.save()
        return HttpResponseRedirect("/lesson_two")
    return render(request, 'fighter/lesson.html', {
        'stack': stack,
        'message': message})

# stack_lesson_one = LessonOne.objects.order_by('?')[0]
# def lesson_one(request):
#     # global stack_lesson_one
#     message = 'The lesson number 1'
#     if request.POST.get('q'):
#         user_english_choice = request.POST['q']
#         print(stack_lesson_one.english, 'original')
#         if user_english_choice == stack_lesson_one.english:
#             print(True)
#             profile = UserProfile.objects.get(user=request.user)
#             profile.points += 2
#             profile.save()
#             stack_lesson_one = LessonOne.objects.order_by('?')[0]
#         elif user_english_choice != stack_lesson_one.english:
#             print(False)
#             stack_lesson_one = LessonOne.objects.order_by('?')[0]
        # return HttpResponseRedirect('/lesson_one')

    # if request.POST.get('plus'):
    #     profile = UserProfile.objects.get(user=request.user)
    #     profile.points += 1
    #     profile.save()
    #     return HttpResponseRedirect("/lesson_one")
    # if request.POST.get('minus'):
    #     print('--' * 8)
    #     print('hello world')
    #     return HttpResponseRedirect("/lesson_one")
    

    # return render(request, "fighter/lesson.html", {
    #     'stack': stack_lesson_one,
    #     'message': message})
# from .models import Profile
# from django import forms
# from django.contrib.auth.forms import UserCreationForm

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = Profile

#     def clean_username(self):
#         username = self.cleaned-data['username']
#         try:

from django.contrib import admin
from .models import (
    LessonOne, LessonTwo, LessonThree,
    LessonFour, LessonFive, LessonSix,
)

class SearchRussianWord(admin.ModelAdmin):
    search_fields = ('russia', 'id')

admin.site.register(LessonOne, SearchRussianWord)
admin.site.register(LessonTwo, SearchRussianWord)
admin.site.register(LessonThree, SearchRussianWord)
admin.site.register(LessonFour, SearchRussianWord)
admin.site.register(LessonFive, SearchRussianWord)
admin.site.register(LessonSix, SearchRussianWord)
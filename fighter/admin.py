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
from .models import LessonOne, LessonTwo

class SearchRussianWord(admin.ModelAdmin):
    search_fields = ('russia', 'id')

admin.site.register(LessonOne, SearchRussianWord)
admin.site.register(LessonTwo, SearchRussianWord)
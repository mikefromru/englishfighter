from django import forms
from .models import (
    LessonOne, 
    LessonTwo,
    LessonThree,
    LessonFour,
    LessonFive,
    LessonSix
)

class LessonOneForm(forms.ModelForm):
    class Meta:
        model = LessonOne
        fields = ('russia', 'english', 'buttons')

class LessonTwoForm(forms.ModelForm):
    class Meta:
        model = LessonTwo
        fields = ('russia', 'english', 'buttons')

class LessonThreeForm(forms.ModelForm):
    class Meta:
        model = LessonThree
        fields = ('russia', 'english', 'buttons')

class LessonFourForm(forms.ModelForm):
    class Meta:
        model = LessonFour
        fields = ('russia', 'english', 'buttons')

class LessonFiveForm(forms.ModelForm):
    class Meta:
        model = LessonFive
        fields = ('russia', 'english', 'buttons')

class LessonSixForm(forms.ModelForm):
    class Meta:
        model = LessonSix
        fields = ('russia', 'english', 'buttons')

# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.db import models

# class RegistrationForm(UserCreationForm):
#     # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))


#     class Meta:
#         model = User
#         fields = ['username']

#     def clean_email(self):
#         email = self.cleaned_data['email']
#         try:
#             User.objects.get(email=email)
#         except User.DoesNotExist:
#             return email
#         raise forms.ValidationError('email already exist')
    
#     def save(self, commit=True):
#         user = super(RegistrationForm, self).save(commit=False)
#         user.username = self.cleaned_data['email']
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.is_active = False
#         user.save()
#         return user


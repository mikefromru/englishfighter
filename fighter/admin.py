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
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile            

class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Доп. информация"

class UserAdmin(UserAdmin):
    inlines = (UserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
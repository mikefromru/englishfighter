from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=30)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Изображения', blank=True, null=True)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
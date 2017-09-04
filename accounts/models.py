from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile')
    points = models.IntegerField(default=0)
    pointsProgressBar = models.IntegerField(default=0)
    city = models.CharField(max_length=30, blank=True)
    about = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', verbose_name='Изображения', blank=True)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


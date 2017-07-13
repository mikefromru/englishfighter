from django.db import models 
# -*- coding: UTF-8 -*-

class LessonOne(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia
    
    class Meta:
        verbose_name = 'LessonOne'

class LessonTwo(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'LessonTwo'


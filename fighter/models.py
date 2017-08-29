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

class LessonThree(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'LessonThree'

class LessonFour(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'LessonFour'

class LessonFive(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'LessonFive'

class LessonSix(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'LessonSix'

class LessonSeven(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'LessonSeven'


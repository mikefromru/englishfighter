from django.db import models 
# -*- coding: UTF-8 -*-

class LessonOne(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia
    
    class Meta:
        verbose_name = 'To be'
        verbose_name_plural = 'To be'

class LessonTwo(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'Past.s, Present.s, Future.s'
        verbose_name_plural = 'Past.s, Present.s, Future.s'

class LessonThree(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'Past.c, Present.c, Future.c'
        verbose_name_plural = 'Past.c, Present.c, Future.c'

class LessonFour(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'Present perfect'
        verbose_name_plural = 'Present perfect'

class LessonFive(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'Some-any, much-muny, few-little'
        verbose_name_plural = 'Some-any, much-muny, few-little'

class LessonSix(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.TextField()

    def __str__(self):
        return self.russia

    class Meta:
        verbose_name = 'LessonSix'
        verbose_name_plural = 'LessonSix'
from django.db import models 

class LessonOne(models.Model):
    russia = models.CharField(max_length=250)
    english = models.CharField(max_length=250)
    buttons = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.russia

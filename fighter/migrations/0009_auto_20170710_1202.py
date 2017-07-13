# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-10 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighter', '0008_lessontwo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessonone',
            options={'verbose_name': 'LessonOne'},
        ),
        migrations.AlterModelOptions(
            name='lessontwo',
            options={'verbose_name': 'LessonTwo'},
        ),
        migrations.AlterField(
            model_name='lessonone',
            name='buttons',
            field=models.TextField(blank=True, max_length=2500),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fighter', '0002_auto_20170410_0530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(blank=True),
        ),
    ]
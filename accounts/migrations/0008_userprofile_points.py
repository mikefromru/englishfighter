# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-20 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20170411_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]

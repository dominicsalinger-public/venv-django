# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 17:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20171105_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='insert_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

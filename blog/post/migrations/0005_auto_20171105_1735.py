# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 17:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20171105_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='insert_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

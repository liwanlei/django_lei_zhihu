# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huati', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hua',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='简述'),
        ),
    ]
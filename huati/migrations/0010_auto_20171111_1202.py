# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huati', '0009_auto_20171111_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hua',
            name='leibie',
            field=models.CharField(choices=[('文章', '文章'), ('提问', '提问')], default='文章', max_length=4),
        ),
    ]
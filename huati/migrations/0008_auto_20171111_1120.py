# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('huati', '0007_auto_20171111_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hua',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]

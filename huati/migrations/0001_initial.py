# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 04:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commenthuati',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='话题评论时间')),
                ('comment', models.TextField(verbose_name='话题评论内容')),
                ('dianzan', models.IntegerField(default=0, verbose_name='点赞')),
                ('status', models.BooleanField(default=False, verbose_name='是否冻结')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='huati.Commenthuati')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '话题评论',
                'verbose_name_plural': '话题评论',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Hua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('connet', models.TextField(verbose_name='话题内容')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='发表时间')),
                ('is_shi', models.BooleanField(default=False, verbose_name='是否匿名')),
                ('status', models.BooleanField(default=False, verbose_name='是否冻结')),
                ('guanzhu_num', models.IntegerField(default=0, verbose_name='关注人数')),
                ('liu_num', models.IntegerField(default=0, verbose_name='浏览人数')),
                ('yaoqing', models.CharField(max_length=255, verbose_name='邀请人')),
                ('leibie', models.CharField(choices=[(0, '提问'), (1, '话题')], max_length=4)),
            ],
            options={
                'verbose_name': '话题',
                'verbose_name_plural': '话题',
                'ordering': ['-time'],
            },
        ),
        migrations.CreateModel(
            name='Huafen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='话题分类')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('status', models.BooleanField(default=False, verbose_name='是否冻结')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '话题分类',
                'verbose_name_plural': '话题分类',
                'ordering': ['-time'],
            },
        ),
        migrations.AddField(
            model_name='hua',
            name='fenlei',
            field=models.ManyToManyField(to='huati.Huafen'),
        ),
        migrations.AddField(
            model_name='hua',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

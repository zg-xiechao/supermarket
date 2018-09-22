# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 10:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateField(auto_now_add=True, verbose_name='添加时间')),
                ('Modify_time', models.DateField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=0, verbose_name='是否删除')),
                ('username', models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('nickname', models.CharField(blank=True, max_length=16, null=True, verbose_name='昵称')),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女'), (3, '保密')], default=3, verbose_name='性别')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('school', models.CharField(blank=True, max_length=50, null=True, verbose_name='学校')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='位置')),
                ('hometown', models.CharField(blank=True, max_length=255, null=True, verbose_name='故乡')),
                ('head_photo', models.ImageField(default='imgages/infortx.png', upload_to='head/%Y/%m')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

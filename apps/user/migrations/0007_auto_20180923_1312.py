# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-23 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180922_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='head_photo',
            field=models.ImageField(default='user/infortx.png', upload_to='user/%Y%m/%d', verbose_name='用户头像'),
        ),
    ]

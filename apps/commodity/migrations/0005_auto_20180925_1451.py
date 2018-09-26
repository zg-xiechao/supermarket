# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commodity', '0004_auto_20180925_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsclassify',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='goodsphoto',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='goods_spu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commodity.GoodsSpu', verbose_name='商品spu_id'),
        ),
        migrations.AlterField(
            model_name='goodssku',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='goodsspu',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='slideshow',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='units',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]
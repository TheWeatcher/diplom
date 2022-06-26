# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-01 15:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20220601_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 6, 1, 18, 23, 47, 301101), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 6, 1, 18, 23, 47, 300104), verbose_name='Опубликован'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
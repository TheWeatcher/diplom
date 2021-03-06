# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-01 15:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20220601_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 6, 1, 18, 40, 40, 850602), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 6, 1, 18, 40, 40, 849605), verbose_name='Опубликован'),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-06-01 14:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220511_2034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='members',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 6, 1, 17, 57, 5, 132550), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 6, 1, 17, 57, 5, 132550), verbose_name='Опубликован'),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-05-11 17:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220511_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='type',
            field=models.CharField(choices=[('D', 'Диалог'), ('C', 'Чат')], default='D', max_length=1, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 5, 11, 20, 34, 23, 364528), verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 5, 11, 20, 34, 23, 364528), verbose_name='Опубликован'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-30 19:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=150, verbose_name=' Email'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=150, verbose_name='Телефон'),
        ),
    ]

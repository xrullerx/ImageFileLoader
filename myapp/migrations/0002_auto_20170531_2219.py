# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]

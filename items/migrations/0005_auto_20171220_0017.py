# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20171219_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='item',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
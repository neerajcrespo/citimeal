# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citimeal', '0016_auto_20180209_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.TextField(max_length=120),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-11 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citimeal', '0021_auto_20180211_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

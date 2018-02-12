# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0008_auto_20171220_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='items/'),
        ),
    ]
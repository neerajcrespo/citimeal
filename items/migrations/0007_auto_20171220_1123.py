# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20171220_1039'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20171220_1039'),
        ('carts', '0004_auto_20171218_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='items',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]

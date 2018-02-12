# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 10:39
from __future__ import unicode_literals

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20171220_1039'),
        ('items', '0005_auto_20171220_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=39.99, max_digits=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='items/')),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-06 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_auto_20161203_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='value',
            field=models.IntegerField(default=0, verbose_name='value'),
            preserve_default=False,
        ),
    ]

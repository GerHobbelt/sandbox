# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160515_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]

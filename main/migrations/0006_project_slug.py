# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-04 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170329_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.CharField(default='asd', max_length=100),
            preserve_default=False,
        ),
    ]

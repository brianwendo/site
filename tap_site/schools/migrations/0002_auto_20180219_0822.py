# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-19 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=2000),
        ),
    ]

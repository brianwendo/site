# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-05 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constituencies', '0003_cluster'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/constituencies/%Y/%m/%d'),
        ),
    ]
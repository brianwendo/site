# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 11:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wards', '0004_auto_20180704_1242'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='preference',
            name='review',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='user',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]

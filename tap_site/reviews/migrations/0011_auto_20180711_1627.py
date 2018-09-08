# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 13:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0010_auto_20180705_1418'),
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
        migrations.RemoveField(
            model_name='review',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='review',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
    ]
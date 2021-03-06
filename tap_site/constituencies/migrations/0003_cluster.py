# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 11:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('constituencies', '0002_auto_20180219_0822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(related_name='constituencies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

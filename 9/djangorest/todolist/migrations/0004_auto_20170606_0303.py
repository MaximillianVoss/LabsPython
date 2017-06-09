# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20170606_0301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='tags',
        ),
        migrations.AddField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(to='todolist.Tag'),
        ),
    ]
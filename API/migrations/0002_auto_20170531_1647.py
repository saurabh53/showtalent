# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 16:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='mediaFile',
        ),
        migrations.RemoveField(
            model_name='post',
            name='videos',
        ),
    ]

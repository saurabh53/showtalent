# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 07:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0006_userprofile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
    ]

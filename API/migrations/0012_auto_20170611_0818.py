# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-11 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0011_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.FileField(blank=True, upload_to='profileImages/'),
        ),
    ]
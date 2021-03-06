# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 16:52
from __future__ import unicode_literals

import API.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_auto_20170611_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='token',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.FileField(blank=True, upload_to=API.models.content_file_name),
        ),
    ]

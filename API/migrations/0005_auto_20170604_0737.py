# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20170602_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
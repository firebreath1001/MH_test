# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-30 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhsite', '0003_auto_20171225_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date_of_birth',
            field=models.CharField(max_length=20),
        ),
    ]
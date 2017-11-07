# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 12:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mhsite', '0002_auto_20171010_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='admission_number',
            field=models.CharField(help_text='1234/17', max_length=7, unique=True, validators=[django.core.validators.RegexValidator(message='The format for admission number is 1234/17', regex='^[0-9]{4}/[0-9]{2}$')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Invalid mobile number', regex='[0-9]{10}')]),
        ),
        migrations.AlterField(
            model_name='application',
            name='pincode',
            field=models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid pincode', regex='^[0-9]{6}$')]),
        ),
    ]
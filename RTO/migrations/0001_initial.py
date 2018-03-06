# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='personal_detail',
            fields=[
                ('user_name', models.CharField(default='satya', max_length=100)),
                ('father_name', models.CharField(default='deep', max_length=100)),
                ('mother_name', models.CharField(default='satya', max_length=100)),
                ('permanent_address', models.CharField(default='satya', max_length=250)),
                ('temporary_address', models.CharField(default='satya', max_length=250)),
                ('district', models.CharField(default='satya', max_length=50)),
                ('state', models.CharField(default='satya', max_length=50)),
                ('duration_stay', models.FloatField(default=0.0, max_length=4)),
                ('pan_no', models.IntegerField(default=None)),
                ('aadhar_no', models.IntegerField(primary_key=True, serialize=False)),
                ('mobile_no', models.IntegerField(default=0)),
                ('email_id', models.EmailField(default='satya', max_length=25)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 14:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RTO', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_detail',
            name='id',
        ),
        migrations.AlterField(
            model_name='personal_detail',
            name='aadhar_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

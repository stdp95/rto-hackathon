# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 18:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RTO', '0002_auto_20180303_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle_detail',
            fields=[
                ('dealer_name', models.CharField(max_length=50)),
                ('dealer_address', models.CharField(max_length=250)),
                ('vehicle_class', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=20)),
                ('vehicle_type', models.CharField(max_length=20)),
                ('company_name', models.CharField(max_length=15)),
                ('year_manufacture', models.IntegerField()),
                ('numberof_cylinders', models.IntegerField()),
                ('horse_power', models.IntegerField()),
                ('cubic_capacity', models.IntegerField()),
                ('chassis_no', models.IntegerField(primary_key=True, serialize=False)),
                ('engine_number', models.IntegerField()),
                ('seating_capacity', models.IntegerField()),
                ('fuel_engine', models.CharField(max_length=20)),
                ('unladen_weight', models.IntegerField()),
                ('body_color', models.CharField(max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RTO.personal_detail')),
            ],
        ),
    ]

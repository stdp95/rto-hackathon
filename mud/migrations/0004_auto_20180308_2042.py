# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-08 20:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mud', '0003_auto_20180308_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermanentAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add1', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='PresentAdd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add1', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
                ('chassis_no', models.CharField(max_length=50)),
                ('engine_number', models.CharField(max_length=100)),
                ('seating_capacity', models.IntegerField()),
                ('fuel_engine', models.CharField(max_length=20)),
                ('unladen_weight', models.IntegerField()),
                ('body_color', models.CharField(max_length=10)),
                ('registration_no', models.CharField(blank=True, default='', max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='personaldetail',
            name='district',
        ),
        migrations.RemoveField(
            model_name='personaldetail',
            name='permanent_address',
        ),
        migrations.RemoveField(
            model_name='personaldetail',
            name='state',
        ),
        migrations.RemoveField(
            model_name='personaldetail',
            name='temporary_address',
        ),
        migrations.AlterField(
            model_name='personaldetail',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehicledetails',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mud.PersonalDetail'),
        ),
        migrations.AddField(
            model_name='presentadd',
            name='user_personal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mud.VehicleDetails'),
        ),
        migrations.AddField(
            model_name='permanentadd',
            name='user_personal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='mud.PersonalDetail'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 10:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uLearnApp', '0005_auto_20170314_1153'),
    ]

    operations = [
        migrations.CreateModel(
            name='lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('duration', models.IntegerField(default=0)),
                ('video_url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='lesson',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2017, 3, 21, 10, 17, 18, 834973)),
        ),
    ]

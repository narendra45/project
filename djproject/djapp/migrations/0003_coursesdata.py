# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-12-13 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0002_contactdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_no', models.IntegerField()),
                ('course_name', models.CharField(max_length=100)),
                ('trainer_name', models.CharField(max_length=100)),
                ('start_date', models.DateField(max_length=100)),
                ('start_time', models.TimeField(max_length=100)),
                ('trainer_exp', models.CharField(max_length=50)),
            ],
        ),
    ]
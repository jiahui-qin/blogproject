# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-20 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181220_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crudeex',
            name='crunumber',
        ),
        migrations.AlterField(
            model_name='crudeex',
            name='mcccnumber',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
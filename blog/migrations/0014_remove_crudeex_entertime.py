# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-04 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20180503_2102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crudeex',
            name='entertime',
        ),
    ]
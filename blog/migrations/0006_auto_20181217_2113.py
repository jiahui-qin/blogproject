# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-17 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181215_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testrecord',
            name='batch',
            field=models.CharField(default='default', max_length=20),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-04 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_crudeex_entertime'),
    ]

    operations = [
        migrations.AddField(
            model_name='crudeex',
            name='entertime',
            field=models.DateTimeField(null=True),
        ),
    ]
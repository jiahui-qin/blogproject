# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-26 10:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bactnumber', models.CharField(max_length=50)),
                ('sourcenum', models.CharField(blank=True, max_length=50)),
                ('genus', models.CharField(max_length=200)),
                ('species', models.CharField(max_length=200)),
                ('chinesename', models.CharField(blank=True, max_length=200)),
                ('recadd', models.CharField(max_length=100)),
                ('orinum', models.CharField(blank=True, max_length=100)),
                ('history', models.CharField(blank=True, max_length=100)),
                ('storetime', models.DateTimeField(auto_now_add=True)),
                ('media', models.CharField(max_length=50)),
                ('getmet', models.CharField(max_length=100)),
                ('modbact', models.CharField(blank=True, max_length=50)),
                ('mianuse', models.CharField(blank=True, max_length=100)),
                ('danger', models.CharField(blank=True, max_length=100)),
                ('comment', models.CharField(blank=True, max_length=500)),
                ('upload', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cpd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpdnumber', models.CharField(max_length=20)),
                ('mass', models.FloatField()),
                ('stru', models.CharField(max_length=50)),
                ('recadd', models.CharField(max_length=100)),
                ('nmr', models.CharField(blank=True, max_length=100)),
                ('ms', models.CharField(blank=True, max_length=100)),
                ('rot', models.CharField(blank=True, max_length=100)),
                ('red', models.CharField(blank=True, max_length=100)),
                ('blue', models.CharField(blank=True, max_length=100)),
                ('media', models.CharField(blank=True, max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='crudeex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mcccnumber', models.CharField(max_length=50)),
                ('chinesename', models.CharField(max_length=200)),
                ('recadd', models.CharField(max_length=100)),
                ('media', models.CharField(max_length=200)),
                ('entertime', models.DateTimeField(auto_now_add=True)),
                ('entervol', models.FloatField()),
                ('entercol', models.FloatField()),
                ('solvent', models.CharField(max_length=100)),
                ('exrmethod', models.CharField(blank=True, max_length=500)),
                ('comment', models.CharField(blank=True, max_length=500)),
                ('frombact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.bact')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='testrecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testtype', models.CharField(max_length=20)),
                ('samst', models.IntegerField(null=True)),
                ('samend', models.IntegerField(null=True)),
                ('solvent', models.CharField(max_length=100)),
                ('mass', models.FloatField()),
                ('volume', models.FloatField()),
                ('conc', models.FloatField()),
                ('testconc', models.FloatField(null=True)),
                ('department', models.CharField(max_length=100)),
                ('sendtime', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=500)),
                ('fromcpd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.cpd')),
                ('fromcru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.crudeex')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cpd',
            name='frombact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.crudeex'),
        ),
        migrations.AddField(
            model_name='cpd',
            name='prov',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

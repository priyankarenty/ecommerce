# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductAVEng', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productaveng',
            name='PriceChangeDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
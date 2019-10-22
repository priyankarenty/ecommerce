# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-29 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductAVEng', '0002_productaveng_pricechangedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productaveng',
            name='AnyOtherFee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='AssetTagPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='BasePriceperUnit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='DeliveryChargeperunit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='FreightCharge',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='MarkupPriceperUnit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='RecycleFee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='Taxes',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='TotalPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='productaveng',
            name='WarrantyPrice',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=100),
        ),
    ]
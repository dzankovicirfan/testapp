# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-13 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0004_auto_20180213_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='duration',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Duration(months)'),
        ),
    ]
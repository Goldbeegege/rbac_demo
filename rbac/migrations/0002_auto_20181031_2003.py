# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='action',
            field=models.CharField(default='', max_length=32),
        ),
    ]
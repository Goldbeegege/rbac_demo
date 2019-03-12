# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u6743\u9650\u540d\u79f0')),
                ('url', models.CharField(max_length=32)),
                ('action', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u89d2\u8272\u540d\u79f0')),
                ('permission', models.ManyToManyField(to='rbac.Permission')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='\u7528\u6237\u540d')),
                ('password', models.CharField(max_length=32)),
                ('role', models.ManyToManyField(to='rbac.Role')),
            ],
        ),
        migrations.AddField(
            model_name='permission',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.PermissionGroup'),
        ),
    ]

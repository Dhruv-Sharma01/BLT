# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-20 21:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20160920_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='domain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.Domain'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-30 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_userrole'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='role',
            field=models.CharField(default='DM', max_length=3),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 18:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('confabulation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='notes',
        ),
    ]
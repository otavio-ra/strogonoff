# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-29 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]

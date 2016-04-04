# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('indication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voters.Person')),
            ],
        ),
    ]

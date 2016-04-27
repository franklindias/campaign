# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-27 15:24
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
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cellphone', models.CharField(max_length=15, verbose_name='celular')),
                ('whatsapp', models.CharField(max_length=15, verbose_name='whatsapp')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='telefone secundario')),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='email')),
                ('facebook', models.URLField(blank=True, verbose_name='facebook')),
                ('street', models.CharField(max_length=50, verbose_name='rua de residência')),
                ('number', models.CharField(max_length=6, verbose_name='número de residência')),
                ('district', models.CharField(max_length=50, verbose_name='Bairro de residência')),
                ('city', models.CharField(default='São Gonçalo do Amarante', max_length=50, verbose_name='cidade de residência')),
                ('state', models.CharField(default='RN', max_length=2, verbose_name='estado de residência')),
                ('localNameVoting', models.CharField(max_length=50, verbose_name='Nome do Local de Votação')),
                ('streetVoting', models.CharField(max_length=50, verbose_name='Rua do Local de Votação')),
                ('numberVoting', models.CharField(max_length=6, verbose_name='Número do Local de Votação')),
                ('districtVoting', models.CharField(max_length=50, verbose_name='Bairro do Local de Votação')),
                ('cityVoting', models.CharField(default='São Gonçalo do Amarante', max_length=50, verbose_name='Cidade do Local de Votação')),
                ('stateVoting', models.CharField(default='RN', max_length=2, verbose_name='Estado do Local de Votação')),
                ('indication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='voters.Person', verbose_name='Indicação')),
            ],
        ),
    ]

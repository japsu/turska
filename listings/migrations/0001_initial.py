# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-16 09:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0029_auto_20170827_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExternalEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(help_text='Tekninen nimi eli "slug" näkyy URL-osoitteissa. Sallittuja merkkejä ovat pienet kirjaimet, numerot ja väliviiva. Teknistä nimeä ei voi muuttaa luomisen jälkeen.', max_length=255, unique=True, validators=[django.core.validators.RegexValidator(message='Tekninen nimi saa sisältää vain pieniä kirjaimia, numeroita sekä väliviivoja.', regex='[a-z0-9-]+')], verbose_name='Tekninen nimi')),
                ('name', models.CharField(max_length=63, verbose_name='Tapahtuman nimi')),
                ('description', models.TextField(blank=True, verbose_name='Kuvaus')),
                ('homepage_url', models.CharField(blank=True, max_length=255, verbose_name='Tapahtuman kotisivu')),
                ('venue_name', models.CharField(blank=True, max_length=63)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=63, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('events', models.ManyToManyField(to='core.Event')),
            ],
        ),
    ]
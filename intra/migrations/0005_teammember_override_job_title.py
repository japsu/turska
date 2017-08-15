# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-15 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intra', '0004_teammember_override_name_display_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='override_job_title',
            field=models.CharField(blank=True, default='', help_text='If set, this will override the job title of this person for this team only. If unset, the job title field will be used. This field will not affect badge printing.', max_length=63, verbose_name='Override job title'),
        ),
    ]

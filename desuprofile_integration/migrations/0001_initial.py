# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20150813_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmationCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=63)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('used_at', models.DateTimeField(null=True, blank=True)),
                ('state', models.CharField(default=b'valid', max_length=8, choices=[(b'valid', 'Kelvollinen'), (b'used', 'K\xe4ytetty'), (b'revoked', 'Mit\xe4t\xf6ity')])),
                ('desuprofile_json', models.TextField()),
                ('person', models.ForeignKey(to='core.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name='Desuprofiilin numero', primary_key=True)),
                ('user', models.ForeignKey(verbose_name='K\xe4ytt\xe4j\xe4', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterIndexTogether(
            name='confirmationcode',
            index_together=set([('person', 'state')]),
        ),
    ]

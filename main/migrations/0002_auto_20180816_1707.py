# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ('service',)},
        ),
        migrations.AlterField(
            model_name='customers',
            name='CCNIT',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='registeredservices',
            name='billNum',
            field=models.CharField(unique=True, max_length=200, default=' ', blank=True),
        ),
        migrations.AlterField(
            model_name='registeredservices',
            name='remission',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='services',
            name='ID_service',
            field=models.CharField(unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='specificservices',
            name='remission',
            field=models.ForeignKey(to='main.registeredServices'),
        ),
        migrations.AlterField(
            model_name='technicians',
            name='id_person',
            field=models.CharField(unique=True, max_length=200),
        ),
    ]

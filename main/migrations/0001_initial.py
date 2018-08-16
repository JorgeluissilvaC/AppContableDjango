# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('CCNIT', models.CharField(max_length=200)),
                ('Department', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('cell', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('ext', models.CharField(blank=True, default='0', max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='registeredServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('remission', models.CharField(max_length=200)),
                ('billNum', models.CharField(blank=True, default=' ', max_length=200)),
                ('dateBill', models.DateTimeField(null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('dateService', models.DateTimeField(default=django.utils.timezone.now)),
                ('Observation', models.CharField(default='Ninguna', max_length=200)),
                ('stateRemission', models.IntegerField(blank=True, default=0)),
                ('paidOut', models.FloatField(blank=True, default=0.0)),
                ('residue', models.FloatField(blank=True, default=0.0)),
                ('estateBill', models.IntegerField(blank=True, default=0)),
                ('customer', models.ForeignKey(to='main.customers')),
            ],
            options={
                'ordering': ('remission',),
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ID_service', models.CharField(max_length=200)),
                ('service', models.CharField(max_length=200)),
                ('value', models.FloatField()),
            ],
            options={
                'ordering': ('ID_service',),
            },
        ),
        migrations.CreateModel(
            name='SpecificServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('remission', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('value', models.FloatField()),
                ('total', models.FloatField()),
                ('generalTotal', models.FloatField()),
                ('IVA', models.FloatField()),
                ('RETEIVA', models.FloatField()),
                ('RETEICA', models.FloatField()),
                ('RETEFUENTE', models.FloatField()),
                ('generalTotalWithTax', models.FloatField()),
                ('service', models.ForeignKey(to='main.Services')),
            ],
            options={
                'ordering': ('remission',),
            },
        ),
        migrations.CreateModel(
            name='Technicians',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('id_person', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('address', models.CharField(default=' ', max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='registeredservices',
            name='service',
            field=models.ManyToManyField(to='main.Services'),
        ),
        migrations.AddField(
            model_name='registeredservices',
            name='technician',
            field=models.ForeignKey(to='main.Technicians'),
        ),
    ]

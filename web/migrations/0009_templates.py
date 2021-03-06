# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_servicelist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('graph_list', models.ManyToManyField(blank=True, null=True, to='web.Graphs')),
                ('service_list', models.ManyToManyField(to='web.ServiceList')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('place', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(unique=True, max_length=150)),
                ('phone_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex=b'^\\d{10}$', message=b"Phone number must be entered in the format: '9012345678'. Up to 10 digits allowed.")])),
                ('comments', models.TextField()),
                ('pickUp', models.ForeignKey(to='aug.PlaceChoice')),
            ],
        ),
    ]

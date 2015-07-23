# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aug', '0003_user_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='region',
            field=models.CharField(max_length=10, choices=[(b'South', b'South'), (b'North', b'North')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aug', '0002_auto_20150722_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.IntegerField(default=1, max_length=1, choices=[(2, b'South'), (1, b'North')]),
            preserve_default=False,
        ),
    ]

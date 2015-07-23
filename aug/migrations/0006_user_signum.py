# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aug', '0005_auto_20150723_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signum',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]

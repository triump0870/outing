# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aug', '0004_auto_20150723_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='comments',
            field=models.TextField(null=True, verbose_name=b'Comments (Optional)', blank=True),
        ),
    ]

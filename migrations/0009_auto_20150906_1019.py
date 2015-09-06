# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LemmingServerApp', '0008_auto_20150906_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='record',
            field=models.FloatField(default=0, db_index=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LemmingServerApp', '0007_auto_20150906_0708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='record',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.DeleteModel(
            name='Ranking',
        ),
    ]

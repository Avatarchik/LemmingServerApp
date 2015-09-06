# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LemmingServerApp', '0004_auto_20150818_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='id',
        ),
        migrations.AlterField(
            model_name='ranking',
            name='user',
            field=models.ForeignKey(primary_key=True, serialize=False, to='LemmingServerApp.User'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LemmingServerApp', '0005_auto_20150906_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='user',
            field=models.ForeignKey(primary_key=True, serialize=False, to='LemmingServerApp.User', unique=True),
        ),
    ]

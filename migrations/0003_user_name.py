# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LemmingServerApp', '0002_remove_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='gilyoung', max_length=30),
            preserve_default=False,
        ),
    ]

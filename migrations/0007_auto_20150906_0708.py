# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('LemmingServerApp', '0006_auto_20150906_0651'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='nickName',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='facebookID',
            new_name='userID',
        ),
        migrations.AddField(
            model_name='user',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 6, 7, 8, 27, 836045, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='userType',
            field=models.CharField(default='facebook', max_length=30),
            preserve_default=False,
        ),
    ]

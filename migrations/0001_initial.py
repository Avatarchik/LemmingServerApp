# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('record', models.IntegerField(default=0, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebookID', models.CharField(max_length=200)),
                ('nickName', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='ranking',
            name='user',
            field=models.ForeignKey(to='LemmingServerApp.User'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20150323_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='recipient',
            field=models.ForeignKey(default=django.utils.timezone.now, to='social.Member', related_name='recipient'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 3, 26, 19, 20, 32, 366894, tzinfo=utc), to='social.Member', related_name='user'),
            preserve_default=False,
        ),
    ]

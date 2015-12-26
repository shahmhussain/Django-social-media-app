# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_member_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='messages',
        ),
        migrations.AddField(
            model_name='messages',
            name='isPrivatemessage',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='recipient',
            field=models.ForeignKey(related_name='recipient', null=True, to='social.Member'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='messages',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='messages',
            name='user',
            field=models.ForeignKey(related_name='user', null=True, to='social.Member'),
            preserve_default=True,
        ),
    ]

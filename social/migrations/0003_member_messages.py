# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_remove_member_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='messages',
            field=models.ManyToManyField(to='social.Messages'),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20150326_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='isPrivatemessage',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insoft', '0006_auto_20150520_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrecord',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='Title', blank=True),
            preserve_default=True,
        ),
    ]

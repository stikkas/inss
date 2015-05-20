# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insoft', '0005_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrecord',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
            preserve_default=True,
        ),
    ]

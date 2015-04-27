# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
        ('insoft', '0003_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='direction',
            name='link',
            field=models.ForeignKey(related_name='+', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
    ]

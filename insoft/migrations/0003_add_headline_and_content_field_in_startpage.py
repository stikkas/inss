# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insoft', '0002_create_startpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='startpage',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, null=True, verbose_name='Content'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='startpage',
            name='headline',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Headline'),
            preserve_default=True,
        ),
    ]

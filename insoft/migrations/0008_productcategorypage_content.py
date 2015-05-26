# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insoft', '0007_auto_20150522_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategorypage',
            name='content',
            field=wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Content', blank=True),
            preserve_default=True,
        ),
    ]

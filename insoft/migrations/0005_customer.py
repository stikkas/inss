# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
        ('insoft', '0004_direction_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=255, verbose_name='Customer Name')),
                ('emblem', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Customer emblem', blank=True, to='wagtailimages.Image', null=True)),
                ('page', models.ForeignKey(related_name='customer_links', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Customer Page', blank=True, to='wagtailcore.Page', null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('insoft', '0002_customerrecord_employeepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('text', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Direction', blank=True)),
                ('icon', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Icon', blank=True, to='wagtailimages.Image', null=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='directions', to='insoft.StartPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'db_table': 'insoft_start_direction',
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insoft', '0009_fix_orderable_models'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('record', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Customer', blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='customers', to='insoft.CustomerPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'db_table': 'insoft_customer_record',
            },
            bases=(models.Model,),
        ),
    ]

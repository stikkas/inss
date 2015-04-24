# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
        ('insoft', '0001_initial'),
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
        migrations.CreateModel(
            name='EmployeePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('background', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Background', blank=True, to='wagtailimages.Image', null=True)),
                ('foreground', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Foreground', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'db_table': 'insoft_employee_page',
                'verbose_name': 'Employee page',
            },
            bases=('wagtailcore.page',),
        ),
    ]

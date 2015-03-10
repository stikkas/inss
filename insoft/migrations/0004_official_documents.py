# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
        ('insoft', '0003_add_headline_and_content_field_in_startpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Description', blank=True)),
            ],
            options={
                'db_table': 'insoft_document_page',
                'verbose_name': 'Document',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DocumentScan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('page', modelcluster.fields.ParentalKey(related_name='scans', to='insoft.DocumentPage')),
                ('scan', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Scan', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'db_table': 'insoft_document_scan',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DocumentsCategoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'db_table': 'insoft_documents_category_page',
                'verbose_name': 'Documents category',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='OfficialDocumentsPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'db_table': 'insoft_official_documents_page',
                'verbose_name': 'Official documents',
            },
            bases=('wagtailcore.page',),
        ),
    ]

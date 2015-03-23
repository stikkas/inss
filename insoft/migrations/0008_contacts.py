# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
        ('insoft', '0007_sort_map_locations_by_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('map', models.CharField(max_length=1000, verbose_name='Map')),
                ('info', wagtail.wagtailcore.fields.RichTextField(verbose_name='Info')),
            ],
            options={
                'db_table': 'insoft_contacts_office',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactsPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('preface', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Preface', blank=True)),
            ],
            options={
                'db_table': 'insoft_contacts_page',
                'verbose_name': 'Contacts page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContactsRequisite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('name', models.CharField(max_length=20, verbose_name='Name')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
                ('page', modelcluster.fields.ParentalKey(related_name='requisites', to='insoft.ContactsPage')),
            ],
            options={
                'db_table': 'insoft_contacts_requisite',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='contactsoffice',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='offices', to='insoft.ContactsPage'),
            preserve_default=True,
        ),
    ]

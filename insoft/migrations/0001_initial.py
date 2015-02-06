# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.wagtailroutablepage.models
import modelcluster.tags
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('taggit', '0001_initial'),
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronologyPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('headline', models.CharField(verbose_name='Headline', blank=True, max_length=100, null=True)),
                ('preface', wagtail.wagtailcore.fields.RichTextField(verbose_name='Preface', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Chronology',
                'db_table': 'insoft_chronology_page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ChronologyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('sort_order', models.IntegerField(editable=False, blank=True, null=True)),
                ('period', models.CharField(verbose_name='Period', max_length=20)),
                ('record', wagtail.wagtailcore.fields.RichTextField(verbose_name='Record')),
                ('page', modelcluster.fields.ParentalKey(related_name='records', to='insoft.ChronologyPage')),
            ],
            options={
                'db_table': 'insoft_chronology_record',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrewmanPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('position', models.CharField(verbose_name='Position', max_length=100)),
                ('bio', wagtail.wagtailcore.fields.RichTextField(verbose_name='Biography')),
                ('face', models.ForeignKey(related_name='+', verbose_name='Face', to='wagtailimages.Image', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
            options={
                'verbose_name': 'Crewman',
                'db_table': 'insoft_crewman_page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CrewPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('headline', models.CharField(verbose_name='Headline', blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Crew',
                'db_table': 'insoft_crew_page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PressEntryPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(verbose_name='Body')),
                ('release_date', models.DateField(verbose_name='Release date')),
                ('feed_image', models.ForeignKey(related_name='+', verbose_name='Feed image', to='wagtailimages.Image', blank=True, on_delete=django.db.models.deletion.SET_NULL, null=True)),
            ],
            options={
                'verbose_name': 'Press entry',
                'db_table': 'insoft_press_entry_page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PressEntryTag',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('content_object', modelcluster.fields.ParentalKey(related_name='tagged_items', to='insoft.PressEntryPage')),
                ('tag', models.ForeignKey(related_name='insoft_pressentrytag_items', to='taggit.Tag')),
            ],
            options={
                'db_table': 'insoft_press_entry_tags',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PressPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Press page',
                'db_table': 'insoft_press_page',
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
                ('headline', models.CharField(verbose_name='Headline', blank=True, max_length=100, null=True)),
                ('content', wagtail.wagtailcore.fields.RichTextField(verbose_name='Content', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Simple page',
                'db_table': 'insoft_simple_page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StartPage',
            fields=[
                ('page_ptr', models.OneToOneField(primary_key=True, parent_link=True, serialize=False, auto_created=True, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'Start page',
                'db_table': 'insoft_start_page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='pressentrypage',
            name='tags',
            field=modelcluster.tags.ClusterTaggableManager(verbose_name='Tags', to='taggit.Tag', through='insoft.PressEntryTag', help_text='A comma-separated list of tags.', blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.contrib.wagtailroutablepage.models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0005_make_filter_spec_unique'),
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChronologyPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=100, null=True, verbose_name='Headline', blank=True)),
                ('preface', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Preface', blank=True)),
            ],
            options={
                'db_table': 'insoft_chronology_page',
                'verbose_name': 'Chronology',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ChronologyRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('period', models.CharField(max_length=20, verbose_name='Period')),
                ('record', wagtail.wagtailcore.fields.RichTextField(verbose_name='Record')),
                ('page', modelcluster.fields.ParentalKey(related_name='records', to='insoft.ChronologyPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'db_table': 'insoft_chronology_record',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ContactsOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('map', models.CharField(max_length=1000, verbose_name='Map')),
                ('info', wagtail.wagtailcore.fields.RichTextField(verbose_name='Info')),
            ],
            options={
                'ordering': ['sort_order'],
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
                'ordering': ['sort_order'],
                'db_table': 'insoft_contacts_requisite',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CrewmanPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('bio', wagtail.wagtailcore.fields.RichTextField(verbose_name='Biography')),
                ('face', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Face', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'db_table': 'insoft_crewman_page',
                'verbose_name': 'Crewman',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CrewPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=100, null=True, verbose_name='Headline', blank=True)),
            ],
            options={
                'db_table': 'insoft_crew_page',
                'verbose_name': 'Crew',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CustomerPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=100, null=True, verbose_name='Headline', blank=True)),
                ('location_on_map', models.CharField(max_length=10, verbose_name='Location on map', choices=[('RU-ALT', '\u0410\u043b\u0442\u0430\u0439\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-AMU', '\u0410\u043c\u0443\u0440\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-ARK', '\u0410\u0440\u0445\u0430\u043d\u0433\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-AST', '\u0410\u0441\u0442\u0440\u0430\u0445\u0430\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-BEL', '\u0411\u0435\u043b\u0433\u043e\u0440\u043e\u0434\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-BRY', '\u0411\u0440\u044f\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-VLA', '\u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-VGG', '\u0412\u043e\u043b\u0433\u043e\u0433\u0440\u0430\u0434\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-VLG', '\u0412\u043e\u043b\u043e\u0433\u043e\u0434\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-VOR', '\u0412\u043e\u0440\u043e\u043d\u0435\u0436\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-YEV', '\u0415\u0432\u0440\u0435\u0439\u0441\u043a\u0430\u044f \u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-ZAB', '\u0417\u0430\u0431\u0430\u0439\u043a\u0430\u043b\u044c\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-IVA', '\u0418\u0432\u0430\u043d\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-IRK', '\u0418\u0440\u043a\u0443\u0442\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KB', '\u041a\u0430\u0431\u0430\u0440\u0434\u0438\u043d\u043e-\u0411\u0430\u043b\u043a\u0430\u0440\u0441\u043a\u0430\u044f \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430'), ('RU-KGD', '\u041a\u0430\u043b\u0438\u043d\u0438\u043d\u0433\u0440\u0430\u0434\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KLU', '\u041a\u0430\u043b\u0443\u0436\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KAM', '\u041a\u0430\u043c\u0447\u0430\u0442\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-KC', '\u041a\u0430\u0440\u0430\u0447\u0430\u0435\u0432\u043e-\u0427\u0435\u0440\u043a\u0435\u0441\u0441\u043a\u0430\u044f \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430'), ('RU-KEM', '\u041a\u0435\u043c\u0435\u0440\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KIR', '\u041a\u0438\u0440\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KOS', '\u041a\u043e\u0441\u0442\u0440\u043e\u043c\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KDA', '\u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-KYA', '\u041a\u0440\u0430\u0441\u043d\u043e\u044f\u0440\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-KGN', '\u041a\u0443\u0440\u0433\u0430\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KRS', '\u041a\u0443\u0440\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-LEN', '\u041b\u0435\u043d\u0438\u043d\u0433\u0440\u0430\u0434\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-LIP', '\u041b\u0438\u043f\u0435\u0446\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-MAG', '\u041c\u0430\u0433\u0430\u0434\u0430\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-MOW', '\u041c\u043e\u0441\u043a\u0432\u0430'), ('RU-MOS', '\u041c\u043e\u0441\u043a\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-MUR', '\u041c\u0443\u0440\u043c\u0430\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-NEN', '\u041d\u0435\u043d\u0435\u0446\u043a\u0438\u0439 \u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('RU-NIZ', '\u041d\u0438\u0436\u0435\u0433\u043e\u0440\u043e\u0434\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-NGR', '\u041d\u043e\u0432\u0433\u043e\u0440\u043e\u0434\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-NVS', '\u041d\u043e\u0432\u043e\u0441\u0438\u0431\u0438\u0440\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-OMS', '\u041e\u043c\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-ORE', '\u041e\u0440\u0435\u043d\u0431\u0443\u0440\u0433\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-ORL', '\u041e\u0440\u043b\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-PNZ', '\u041f\u0435\u043d\u0437\u0435\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-PER', '\u041f\u0435\u0440\u043c\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-PRI', '\u041f\u0440\u0438\u043c\u043e\u0440\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-PSK', '\u041f\u0441\u043a\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-AD', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0410\u0434\u044b\u0433\u0435\u044f (\u0410\u0434\u044b\u0433\u0435\u044f)'), ('RU-AL', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0410\u043b\u0442\u0430\u0439'), ('RU-BA', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0411\u0430\u0448\u043a\u043e\u0440\u0442\u043e\u0441\u0442\u0430\u043d'), ('RU-BU', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0411\u0443\u0440\u044f\u0442\u0438\u044f'), ('RU-DA', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0414\u0430\u0433\u0435\u0441\u0442\u0430\u043d'), ('RU-IN', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0418\u043d\u0433\u0443\u0448\u0435\u0442\u0438\u044f'), ('RU-KL', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u041a\u0430\u043b\u043c\u044b\u043a\u0438\u044f'), ('RU-KR', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u041a\u0430\u0440\u0435\u043b\u0438\u044f'), ('RU-KO', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u041a\u043e\u043c\u0438'), ('RU-KRM', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u041a\u0440\u044b\u043c'), ('RU-ME', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u041c\u0430\u0440\u0438\u0439 \u042d\u043b'), ('RU-MO', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u041c\u043e\u0440\u0434\u043e\u0432\u0438\u044f'), ('RU-SA', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0421\u0430\u0445\u0430 (\u042f\u043a\u0443\u0442\u0438\u044f)'), ('RU-SE', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0421\u0435\u0432\u0435\u0440\u043d\u0430\u044f \u041e\u0441\u0435\u0442\u0438\u044f-\u0410\u043b\u0430\u043d\u0438\u044f'), ('RU-TA', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0422\u0430\u0442\u0430\u0440\u0441\u0442\u0430\u043d (\u0422\u0430\u0442\u0430\u0440\u0441\u0442\u0430\u043d)'), ('RU-TY', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0422\u044b\u0432\u0430'), ('RU-KK', '\u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 \u0425\u0430\u043a\u0430\u0441\u0438\u044f'), ('RU-ROS', '\u0420\u043e\u0441\u0442\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-RYA', '\u0420\u044f\u0437\u0430\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-SAM', '\u0421\u0430\u043c\u0430\u0440\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-SPE', '\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433'), ('RU-SAR', '\u0421\u0430\u0440\u0430\u0442\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-SAK', '\u0421\u0430\u0445\u0430\u043b\u0438\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-SVE', '\u0421\u0432\u0435\u0440\u0434\u043b\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-SEV', '\u0421\u0435\u0432\u0430\u0441\u0442\u043e\u043f\u043e\u043b\u044c'), ('RU-SMO', '\u0421\u043c\u043e\u043b\u0435\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-STA', '\u0421\u0442\u0430\u0432\u0440\u043e\u043f\u043e\u043b\u044c\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-TAM', '\u0422\u0430\u043c\u0431\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-TVE', '\u0422\u0432\u0435\u0440\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-TOM', '\u0422\u043e\u043c\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-TUL', '\u0422\u0443\u043b\u044c\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-TYU', '\u0422\u044e\u043c\u0435\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-UD', '\u0423\u0434\u043c\u0443\u0440\u0442\u0441\u043a\u0430\u044f \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430'), ('RU-ULY', '\u0423\u043b\u044c\u044f\u043d\u043e\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-KHA', '\u0425\u0430\u0431\u0430\u0440\u043e\u0432\u0441\u043a\u0438\u0439 \u043a\u0440\u0430\u0439'), ('RU-KHM', '\u0425\u0430\u043d\u0442\u044b-\u041c\u0430\u043d\u0441\u0438\u0439\u0441\u043a\u0438\u0439 \u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433 - \u042e\u0433\u0440\u0430'), ('RU-CHE', '\u0427\u0435\u043b\u044f\u0431\u0438\u043d\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c'), ('RU-CE', '\u0427\u0435\u0447\u0435\u043d\u0441\u043a\u0430\u044f \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430'), ('RU-CU', '\u0427\u0443\u0432\u0430\u0448\u0441\u043a\u0430\u044f \u0420\u0435\u0441\u043f\u0443\u0431\u043b\u0438\u043a\u0430 - \u0427\u0443\u0432\u0430\u0448\u0438\u044f'), ('RU-CHU', '\u0427\u0443\u043a\u043e\u0442\u0441\u043a\u0438\u0439 \u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('RU-YAN', '\u042f\u043c\u0430\u043b\u043e-\u041d\u0435\u043d\u0435\u0446\u043a\u0438\u0439 \u0430\u0432\u0442\u043e\u043d\u043e\u043c\u043d\u044b\u0439 \u043e\u043a\u0440\u0443\u0433'), ('RU-YAR', '\u042f\u0440\u043e\u0441\u043b\u0430\u0432\u0441\u043a\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c')])),
                ('content', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Content', blank=True)),
            ],
            options={
                'db_table': 'insoft_customer_page',
                'verbose_name': 'Customer page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CustomersPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'db_table': 'insoft_customers_page',
                'verbose_name': 'Customers page',
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
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
                'ordering': ['sort_order'],
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
        migrations.CreateModel(
            name='PressEntryPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField(verbose_name='Body')),
                ('release_date', models.DateField(verbose_name='Release date')),
                ('feed_image', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Feed image', blank=True, to='wagtailimages.Image', null=True)),
            ],
            options={
                'db_table': 'insoft_press_entry_page',
                'verbose_name': 'Press entry',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PressEntryTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'db_table': 'insoft_press_page',
                'verbose_name': 'Press page',
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ProductCategoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'db_table': 'insoft_product_category_page',
                'verbose_name': 'Product category page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductLinkPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'db_table': 'insoft_product_link_page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Content', blank=True)),
            ],
            options={
                'db_table': 'insoft_product_page',
                'verbose_name': 'Product page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductsPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Content', blank=True)),
            ],
            options={
                'db_table': 'insoft_products_page',
                'verbose_name': 'Products page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProductSubCategoryPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'db_table': 'insoft_product_subcategory_page',
                'verbose_name': 'Product subcategory page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=100, null=True, verbose_name='Headline', blank=True)),
                ('content', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Content', blank=True)),
            ],
            options={
                'db_table': 'insoft_simple_page',
                'verbose_name': 'Simple page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='StartPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('headline', models.CharField(max_length=100, null=True, verbose_name='Headline', blank=True)),
                ('content', wagtail.wagtailcore.fields.RichTextField(null=True, verbose_name='Content', blank=True)),
            ],
            options={
                'db_table': 'insoft_start_page',
                'verbose_name': 'Start page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='productlinkpage',
            name='link',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Link', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pressentrypage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(to='taggit.Tag', through='insoft.PressEntryTag', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contactsoffice',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='offices', to='insoft.ContactsPage'),
            preserve_default=True,
        ),
    ]

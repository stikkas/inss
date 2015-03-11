# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0011_equate_slug_length_with_title_length'),
        ('insoft', '0005_customers'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='productlinkpage',
            name='link',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Link', blank=True, to='wagtailcore.Page', null=True),
            preserve_default=True,
        ),
    ]

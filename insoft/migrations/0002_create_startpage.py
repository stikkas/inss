# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_startpage(apps, schema_editor):
    # Get models
    ContentType = apps.get_model('contenttypes.ContentType')
    Page = apps.get_model('wagtailcore.Page')
    Site = apps.get_model('wagtailcore.Site')
    StartPage = apps.get_model('insoft.StartPage')

    # Delete the default startpage
    Page.objects.get(id=2).delete()

    # Create content type for startpage model
    startpage_content_type, created = ContentType.objects.get_or_create(
        model='startpage', app_label='insoft', defaults={'name': 'Start page'})

    # Create a new startpage
    startpage = StartPage.objects.create(
        title="Главная",
        slug='home',
        content_type=startpage_content_type,
        path='00010001',
        depth=2,
        numchild=0,
        url_path='/home/',
    )

    # Create a site with the new startpage set as the root
    Site.objects.create(
        hostname='localhost', root_page=startpage, is_default_site=True)


class Migration(migrations.Migration):

    dependencies = [
        ('insoft', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_startpage),
    ]

import datetime
import time

from django.conf.urls import url
from django.db import models
from django.http import Http404
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import Tag, TaggedItemBase


HEADLINE_LEN = 100
LAST_ENTRIES_ON_PAGE = 20


# Start page
class StartPage(Page):
    class Meta:
        db_table = 'insoft_start_page'
        verbose_name = _('Start page')


# Simple page
class SimplePage(Page):
    headline = models.CharField(_('Headline'), max_length=HEADLINE_LEN, blank=True, null=True)
    content = RichTextField(_('Content'), blank=True, null=True)

    class Meta:
        db_table = 'insoft_simple_page'
        verbose_name = _('Simple page')

SimplePage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('headline', classname='full title'),
    FieldPanel('content', classname='full'),
]


# Chronology
class ChronologyRecord(Orderable):
    page = ParentalKey('insoft.ChronologyPage', related_name='records')
    period = models.CharField(_('Period'), max_length=20)
    record = RichTextField(_('Record'))

    panels = [
        FieldPanel('period'),
        FieldPanel('record')
    ]

    class Meta:
        db_table = 'insoft_chronology_record'


class ChronologyPage(Page):
    subpage_types = []

    headline = models.CharField(_('Headline'), max_length=HEADLINE_LEN, blank=True, null=True)
    preface = RichTextField(_('Preface'), blank=True, null=True)

    class Meta:
        db_table = 'insoft_chronology_page'
        verbose_name = _('Chronology')

ChronologyPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('headline', classname='full title'),
    FieldPanel('preface', classname='full'),
    InlinePanel(ChronologyPage, 'records', label=_('Records')),
]


# Crew
class CrewmanPage(Page):
    subpage_types = []

    name = models.CharField(_('Name'), max_length=100)
    face = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Face'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    position = models.CharField(_('Position'), max_length=100)
    bio = RichTextField(_('Biography'))

    class Meta:
        db_table = 'insoft_crewman_page'
        verbose_name = _('Crewman')

CrewmanPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('name', classname='full title'),
    ImageChooserPanel('face'),
    FieldPanel('position', classname='full title'),
    FieldPanel('bio', classname='full')
]


class CrewPage(Page):
    subpage_types = ['insoft.CrewmanPage']

    headline = models.CharField(_('Headline'), max_length=HEADLINE_LEN, blank=True, null=True)

    @property
    def members(self):
        return CrewmanPage.objects.filter(live=True)

    class Meta:
        db_table = 'insoft_crew_page'
        verbose_name = _('Crew')

CrewPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('headline', classname='full title'),
]


# Press
class PressPage(RoutablePageMixin, Page):
    subpage_types = ['insoft.PressEntryPage']
    subpage_urls = (
        url(r'^$', 'latest', name='latest'),
        url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', 'archive', name='archive'),
    )

    @property
    def last_entries(self):
        return PressEntryPage.objects.filter(
            live=True,
        ).order_by('-release_date').only('title', 'release_date', 'url_path')[:LAST_ENTRIES_ON_PAGE]

    def latest(self, request):
        return render(request, self.template, {'self': self})

    def archive(self, request, year, month):
        try:
            t = time.strptime('%s-%s' % (year, month), '%Y-%m')
            selected_date = datetime.date(*t[:3])
        except ValueError:
            raise Http404

        entries = PressEntryPage.objects.filter(
            live=True,
            release_date__year=selected_date.year,
            release_date__month=selected_date.month
        )
        if not entries.exists():
            raise Http404

        return render(request, 'insoft/press_archive_page.html', {
            'entries': entries,
            'self': self,
            'selected_date': selected_date
        })

    class Meta:
        db_table = 'insoft_press_page'
        verbose_name = _('Press page')


class PressEntryTag(TaggedItemBase):
    content_object = ParentalKey('insoft.PressEntryPage', related_name='tagged_items')

    class Meta:
        db_table = 'insoft_press_entry_tags'


class PressEntryPage(Page):
    subpage_types = []

    body = RichTextField(_('Body'))
    tags = ClusterTaggableManager(through=PressEntryTag, blank=True)
    release_date = models.DateField(_('Release date'))
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Feed image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    class Meta:
        db_table = 'insoft_press_entry_page'
        verbose_name = _('Press entry')

PressEntryPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('release_date'),
    FieldPanel('body', classname='full'),
    ImageChooserPanel('feed_image'),
    FieldPanel('tags')
]

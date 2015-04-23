
# encoding: utf-8
import datetime
import time

from django.conf.urls import url
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                PageChooserPanel)
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag

from insoft import maps


HEADLINE_LEN = 100
LAST_ENTRIES_ON_PAGE = 20


# Start page
class StartPage(Page):
    headline = models.CharField(_('Headline'), max_length=HEADLINE_LEN, blank=True, null=True)
    content = RichTextField(_('Content'), blank=True, null=True)

    class Meta:
        db_table = 'insoft_start_page'
        verbose_name = _('Start page')

StartPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('headline', classname='full title'),
    FieldPanel('content', classname='full'),
]


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
        ordering = ['sort_order']


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


# Official Documents
class OfficialDocumentsPage(Page):
    subpage_types = ['insoft.DocumentsCategoryPage']

    @property
    def categories(self):
        return DocumentsCategoryPage.objects.child_of(self)

    class Meta:
        db_table = 'insoft_official_documents_page'
        verbose_name = _('Official documents')


class DocumentsCategoryPage(Page):
    subpage_types = ['insoft.DocumentPage']

    @property
    def documents(self):
        return DocumentPage.objects.child_of(self).prefetch_related('scans__scan')

    class Meta:
        db_table = 'insoft_documents_category_page'
        verbose_name = _('Documents category')


class DocumentScan(Orderable):
    page = ParentalKey('insoft.DocumentPage', related_name='scans')
    scan = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Scan'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('scan')
    ]

    class Meta:
        db_table = 'insoft_document_scan'
        ordering = ['sort_order']


class DocumentPage(Page):
    subpage_types = []
    description = models.CharField(_('Description'), max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'insoft_document_page'
        verbose_name = _('Document')

DocumentPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('description', classname='full'),
    InlinePanel(DocumentPage, 'scans', label=_('Scans'))
]


# Customers
class CustomersPage(RoutablePageMixin, Page):
    subpage_types = ['insoft.CustomerPage']
    subpage_urls = (
        url(r'^$', 'map', name='customers_map'),
        url(r'^location/(?P<location_code>ru-mow|ru-spe)/$',
            'fed_cust_on_location', name='customers_on_location'),
        url(r'^location/(?P<location_code>[a-z-]{2,10})/$',
            'customers_on_location', name='customers_on_location'),
    )

    def map(self, request):
        return render(request, self.template, {'self': self})

    # В Москве и Питере несколько страниц
    def fed_cust_on_location(self, request, location_code):
        location = maps.get_location(maps.RUSSIA, location_code)
        if not location:
            raise Http404

        customers = CustomerPage.objects.filter(
            live=True,
            location_on_map=location.code
        ).defer('title')
        return self._return_lp(request, customers, location)

    def customers_on_location(self, request, location_code):
        location = maps.get_location(maps.RUSSIA, location_code)
        if not location:
            raise Http404

        customers = CustomerPage.objects.filter(
            live=True,
            location_on_map=location.code
        ).defer('title')

        if len(customers) > 0:
            # На один регион одна страница
            return HttpResponseRedirect(customers[0].relative_url(request.site))

        # Значит в регионе нет заказчиков
        return self._return_lp(request, customers, location)

    def _return_lp(self, request, customers, location):
        return render(request, 'insoft/customers_on_location_page.html', {
            'customers': customers,
            'self': self,
            'location': location
        })

    class Meta:
        db_table = 'insoft_customers_page'
        verbose_name = _('Customers page')


class CustomerRecord(Orderable):
    page = ParentalKey('insoft.CustomerPage', related_name='customers')
    title = models.CharField(_('Title'), max_length=100)
    record = RichTextField(_('Customer'), blank=True, null=True)

    panels = [
        FieldPanel('title', classname='full title'),
        FieldPanel('record', classname='full'),
    ]

    class Meta:
        db_table = 'insoft_customer_record'
        ordering = ['sort_order']


class CustomerPage(Page):
    headline = models.CharField(_('Headline'), max_length=HEADLINE_LEN, blank=True, null=True)
    location_on_map = models.CharField(_('Location on map'), max_length=10,
                                       choices=maps.choices(maps.RUSSIA))
    content = RichTextField(_('Content'), blank=True, null=True)

    class Meta:
        db_table = 'insoft_customer_page'
        verbose_name = _('Customer page')

CustomerPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('headline', classname='full title'),
    FieldPanel('location_on_map', classname='full title'),
    FieldPanel('content', classname='full'),
    InlinePanel(CustomerPage, 'customers', label=_('Customers')),
]


# Products
class ProductsPage(Page):
    subpage_types = ['insoft.ProductCategoryPage']

    content = RichTextField(_('Content'), blank=True, null=True)

    class Meta:
        db_table = 'insoft_products_page'
        verbose_name = _('Products page')

ProductsPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('content', classname='full'),
]


class ProductCategoryPage(Page):
    subpage_types = ['insoft.ProductSubCategoryPage',
                     'insoft.ProductPage',
                     'insoft.ProductLinkPage']

    @property
    def products(self):
        return self.get_children().not_type(ProductSubCategoryPage)

    class Meta:
        db_table = 'insoft_product_category_page'
        verbose_name = _('Product category page')


class ProductSubCategoryPage(Page):
    subpage_types = ['insoft.ProductPage', 'insoft.ProductLinkPage']

    @property
    def products(self):
        return self.get_children()

    class Meta:
        db_table = 'insoft_product_subcategory_page'
        verbose_name = _('Product subcategory page')


class ProductPage(Page):
    subpage_types = []

    content = RichTextField(_('Content'), blank=True, null=True)

    class Meta:
        db_table = 'insoft_product_page'
        verbose_name = _('Product page')

ProductPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('content', classname='full'),
]


class ProductLinkPage(Page):
    link = models.ForeignKey(
        'wagtailcore.Page',
        verbose_name=_('Link'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    @property
    def content(self):
        return ProductPage.objects.get(id=self.link.id).content

    class Meta:
        db_table = 'insoft_product_link_page'

ProductLinkPage.content_panels = [
    FieldPanel('title', classname='full title'),
    PageChooserPanel('link', 'insoft.ProductPage')
]


# Press
class PressPage(RoutablePageMixin, Page):
    subpage_types = ['insoft.PressEntryPage']
    subpage_urls = (
        url(r'^$', 'latest', name='latest'),
        url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', 'archive', name='archive'),
        url(r'^tag/(?P<tag>[0-9]+)/$', 'show_tag', name='show-tag'),
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

    def show_tag(self, request, tag):
        entries = PressEntryTag.objects.filter(tag_id=tag)
        if not entries.exists():
            raise Http404

        return render(request, 'insoft/press_tag_page.html', {
            'entries': [it.content_object for it in entries],
            'self': self,
            'tag_name': Tag.objects.get(id=tag).name
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


# Contacts
class ContactsOffice(Orderable):
    page = ParentalKey('insoft.ContactsPage', related_name='offices')
    map = models.CharField(_('Map'), max_length=1000)
    info = RichTextField(_('Info'))

    panels = [
        FieldPanel('map', classname='full'),
        FieldPanel('info', classname='full')
    ]

    class Meta:
        db_table = 'insoft_contacts_office'
        ordering = ['sort_order']


class ContactsRequisite(Orderable):
    page = ParentalKey('insoft.ContactsPage', related_name='requisites')
    name = models.CharField(_('Name'), max_length=20)
    value = models.CharField(_('Value'), max_length=255)

    panels = [
        FieldPanel('name', classname='full'),
        FieldPanel('value', classname='full')
    ]

    class Meta:
        db_table = 'insoft_contacts_requisite'
        ordering = ['sort_order']


class ContactsPage(Page):
    preface = RichTextField(_('Preface'), null=True, blank=True)

    class Meta:
        db_table = 'insoft_contacts_page'
        verbose_name = _('Contacts page')

ContactsPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('preface', classname='full'),
    InlinePanel(ContactsPage, 'offices', label=_('Offices')),
    InlinePanel(ContactsPage, 'requisites', label=_('Requisites'))
]

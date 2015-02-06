import os
import datetime

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from lxml.html import fromstring, tostring
from lxml.html.clean import clean_html

from insoft.models import PressPage, PressEntryPage


def migrate(data_dir, page_id):
    press_page = PressPage.objects.get(id=page_id)

    with open(os.path.join(data_dir, 'index.txt'), 'r', encoding='cp1251') as index_file:
        index_news = index_file.read()

    index_news = index_news.splitlines()
    index_news.reverse()

    for news_entity in index_news:
        file_name, date, title = news_entity.split('^')

        try:
            with open(os.path.join(data_dir, file_name), 'rb') as news_file:
                html_news = news_file.read()
        except IOError as e:
            if e.errno != 2:
                raise
            print("File not found: %s" % file_name)
            continue

        try:
            html_news = html_news.decode('cp1251')
        except UnicodeEncodeError:
            print("Bad coding in file: %s" % file_name)
            continue

        dom_tree = fromstring(html_news)

        try:
            content = dom_tree.xpath('/html/body/div/table/tr[2]/td[2]/table/tr[1]/td')[0]
        except IndexError:
            print("Bad structure in file: %s" % file_name)
            continue

        content.tag = 'div'
        if content.attrib.get('valign'):
            del content.attrib['valign']

        # Clear span tags
        for s in content.xpath('//span'):
            if s.attrib.get('style'):
                if s.attrib['style'].find('font-weight') != -1:
                    style = s.attrib['style'].replace(' ', '')
                    if style.find('font-weight:700') != -1 or style.find('font-weight:bold') != -1:
                        s.tag = 'strong'
                    del s.attrib['style']
                else:
                    s.drop_tag()
            else:
                s.drop_tag()

        for s in content.xpath('//strong'):
            if s.attrib.get('style'):
                if s.attrib['style'].find('font-weight') != -1:
                    style = s.attrib['style'].replace(' ', '')
                    if style.find('font-weight:400') != -1 or style.find('font-weight:normal') != -1:
                        s.drop_tag()

        content = clean_html(content)

        # Clear  class="MsoNormal" and etc
        for p in content.xpath('//p'):
            if p.attrib.get('class'):
                del p.attrib['class']

        # Clear attributes width and height in tables
        for t in content.xpath('//table'):
            if t.attrib.get('width'): del t.attrib['width']
            if t.attrib.get('height'): del t.attrib['height']
            if t.attrib.get('border'): del t.attrib['border']
            if t.attrib.get('cellspacing'): del t.attrib['cellspacing']
            if t.attrib.get('cellpadding'): del t.attrib['cellpadding']
            if t.attrib.get('class'): del t.attrib['class']
            t.attrib['class'] = 'table table-bordered'

        for td in content.xpath('//td'):
            if td.attrib.get('width'): del td.attrib['width']
            if td.attrib.get('height'): del td.attrib['height']
            if td.attrib.get('class'): del td.attrib['class']
            if td.attrib.get('nowrap'): del td.attrib['nowrap']

        # Prepare to write in DB
        day, month, year = map(int, date.split('.'))
        year += 2000
        date = datetime.date(day=day, month=month, year=year)

        # Cut title
        if len(title) > 120:
            title = title[:117] + '...'

        press_entry = PressEntryPage(
            title=title,
            slug=slugify(file_name),
            body=tostring(content, encoding='utf-8', pretty_print=True),
            release_date=date,
        )
        press_page.add_child(instance=press_entry)


class Command(BaseCommand):
    def handle(self, data_dir, page_id, *args, **options):
        migrate(data_dir, page_id)

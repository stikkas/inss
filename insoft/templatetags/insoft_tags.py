import itertools
from django import template
from django.contrib.contenttypes.models import ContentType
from django.db.models import Count, Q
from taggit.models import Tag

from insoft.models import (
    PressPage, PressEntryPage, PressEntryTag,
    ProductsPage, ProductCategoryPage, ProductSubCategoryPage,
    ProductPage, ProductLinkPage, Customer
)


register = template.Library()


@register.inclusion_tag('insoft/tags/main_menu.html', takes_context=True)
def main_menu(context, current_page):
    root_page = context['request'].site.root_page
    children = root_page.get_children().filter(
        live=True,
        show_in_menus=True
    )
    menu_items = list(itertools.chain([root_page], children))

    selected = None
    for menu_item in menu_items:
        if current_page.url.startswith(menu_item.url):
            selected = menu_item

    return {
        'menu_items': menu_items,
        'selected': selected,
        'request': context['request']
    }


@register.inclusion_tag('insoft/tags/left_menu.html', takes_context=True)
def left_menu(context, current_page, title=None):
    if current_page.get_depth() > 3:
        menu_root = current_page.get_ancestors().get(depth=3)
    else:
        menu_root = current_page

    menu_items = menu_root.get_children().filter(
        live=True,
        show_in_menus=True
    )

    selected = None
    for menu_item in menu_items:
        if current_page.url.startswith(menu_item.url):
            selected = menu_item

    return {
        'title': title or menu_root.title,
        'menu_items': menu_items,
        'selected': selected,
        'request': context['request']
    }


@register.inclusion_tag('insoft/tags/press_archive_date_filter.html', takes_context=True)
def press_archive(context):
    dates = PressEntryPage.objects.filter(
        live=True
    ).dates('release_date', 'month', order='DESC')
    return {
        'dates': dates,
        'request': context['request'],
        'self': context['self'],
        'selected_date': context.get('selected_date')
    }


@register.inclusion_tag('insoft/tags/news_widget.html', takes_context=True)
def news_widget(context, news=2, cnews=3):
    news_entries = PressEntryPage.objects.filter(
        live=True
    ).order_by('-release_date')[:news]
    # TODO: logging case when PressPage not exists or more than one
    try:
        news_page = PressPage.objects.all()[0]
    except IndexError:
        news_page = None
    return {
        'news_entries': news_entries,
        'cnews_entries': cnews,
        'news_page': news_page,
        'request': context['request']
    }


def get_weight_fun(t_min, t_max, f_min, f_max):
    def weight_fun(f_i, t_min=t_min, t_max=t_max, f_min=f_min, f_max=f_max):
        if f_max == f_min:
            mult_fac = 1.0
        else:
            mult_fac = float(t_max-t_min)/float(f_max-f_min)

        return t_max - (f_max-f_i)*mult_fac
    return weight_fun


@register.inclusion_tag('insoft/tags/news_tags_cloud.html', takes_context=True)
def news_tags_cloud(context):
    tag_list = Tag.objects.filter(
        id__in=PressEntryTag.objects.all().values_list('tag_id', flat=True)
    ).annotate(num_times=Count('insoft_pressentrytag_items')).order_by('?')

    num_times = tag_list.values_list('num_times', flat=True)
    weight_fun = get_weight_fun(1.0, 5.0, len(num_times), len(num_times))
    for tag in tag_list:
        tag.weight = weight_fun(tag.num_times)

    return {
        'tag_list': tag_list,
        'request': context['request']
    }


@register.inclusion_tag('insoft/tags/solutions_menu.html', takes_context=True)
def solutions_menu(context, current_page):
    if isinstance(current_page, ProductsPage):
        root_page = current_page
    else:
        root_page = current_page.get_ancestors().type(ProductsPage)[0]

    cat_ct = ContentType.objects.get_for_model(ProductCategoryPage)
    subcat_ct = ContentType.objects.get_for_model(ProductSubCategoryPage)

    pages = root_page.get_descendants().filter(
        Q(content_type=cat_ct) | Q(content_type=subcat_ct)
    ).filter(
        live=True,
        show_in_menus=True
    ).order_by('path')

    menu_items = []
    for page in pages:
        if page.content_type_id == cat_ct.id:
            page.submenu_items = []
            menu_items.append(page)
        if page.content_type_id == subcat_ct.id:
            menu_items[-1].submenu_items.append(page)

    if current_page.__class__ in [ProductPage, ProductLinkPage]:
        selected = current_page.get_parent()
    else:
        selected = current_page

    return {
        'menu_items': menu_items,
        'self': current_page,
        'selected': selected,
        'root_page': root_page,
        'request': context['request']
    }


# Customer snippets
@register.inclusion_tag('insoft/tags/clients.html', takes_context=True)
def clients(context):
    return {
        'customer_links': Customer.objects.select_related('page'),
        'request': context['request'],
    }


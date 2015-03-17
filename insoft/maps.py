# -*- coding: utf-8 -*-
import json
import threading
from collections import namedtuple

from django.contrib.staticfiles.finders import AppDirectoriesFinder


_cache = threading.local()


RUSSIA = 'russia'


Location = namedtuple('Location', ('code', 'name',))


def _load_map(map_name):
    finder = AppDirectoriesFinder(app_names=['insoft'])
    map_file = finder.find('insoft/maps/%s.json' % map_name)
    with open(map_file) as f:
        data = json.loads(f.read())
        paths = sorted(data['pathes'].iteritems(), key=lambda l: l[1]['name'])
        locations = tuple([Location(key, val['name']) for key, val in paths])
        setattr(_cache, map_name, locations)


def get_map(map_name):
    if not hasattr(_cache, map_name):
        _load_map(map_name)
    return getattr(_cache, map_name)


def get_location(map_name, code):
    locations = get_map(map_name)
    for l in locations:
        if l.code.upper() == code.upper():
            return l


def choices(map_name):
    for l in get_map(map_name):
        yield (l.code, l.name,)

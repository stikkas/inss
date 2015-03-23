# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insoft', '0008_contacts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chronologyrecord',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='contactsoffice',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='contactsrequisite',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='documentscan',
            options={'ordering': ['sort_order']},
        ),
    ]

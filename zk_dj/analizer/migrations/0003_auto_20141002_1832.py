# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analizer', '0002_auto_20141002_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='corp',
            field=models.ForeignKey(related_name=b'pilots', on_delete=django.db.models.deletion.SET_NULL, default=None, to='analizer.corp', null=True),
        ),
    ]

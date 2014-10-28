# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analizer', '0003_auto_20141017_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kill',
            name='allianceName',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analizer', '0002_auto_20141017_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attacker',
            name='allianceName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='attacker',
            name='characterName',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

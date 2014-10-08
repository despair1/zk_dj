# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analizer', '0004_auto_20141004_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attacker',
            name='allianceID',
            field=models.ForeignKey(related_name=b'attackers', to='analizer.alli', null=True),
        ),
        migrations.AlterField(
            model_name='kill',
            name='allianceID',
            field=models.ForeignKey(related_name=b'victim', to='analizer.alli', null=True),
        ),
    ]

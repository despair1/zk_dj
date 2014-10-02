# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='corp',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pilot',
            name='corp',
            field=models.ForeignKey(related_name=b'pilots', on_delete=django.db.models.deletion.SET_NULL, default=None, to='analizer.pilot', null=True),
            preserve_default=True,
        ),
    ]

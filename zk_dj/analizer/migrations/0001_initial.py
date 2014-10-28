# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alli',
            fields=[
                ('allianceID', models.IntegerField(serialize=False, primary_key=True)),
                ('allianceName', models.CharField(max_length=255)),
                ('cached', models.DateTimeField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='attacker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('corporationID', models.IntegerField()),
                ('allianceID', models.IntegerField()),
                ('characterID', models.IntegerField()),
                ('securityStatus', models.FloatField()),
                ('weaponTypeID', models.IntegerField()),
                ('finalBlow', models.IntegerField()),
                ('shipTypeID', models.IntegerField()),
                ('corporationName', models.CharField(max_length=255)),
                ('characterName', models.CharField(max_length=255)),
                ('allianceName', models.CharField(max_length=255)),
                ('killTime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='corp',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('cached', models.DateTimeField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='kill',
            fields=[
                ('killID', models.IntegerField(serialize=False, primary_key=True)),
                ('killTime', models.DateTimeField()),
                ('solarSystemID', models.IntegerField()),
                ('corporationName', models.CharField(max_length=255)),
                ('characterName', models.CharField(max_length=255)),
                ('allianceName', models.CharField(max_length=255)),
                ('corporationID', models.IntegerField()),
                ('allianceID', models.IntegerField()),
                ('characterID', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='pilot',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('cached', models.DateTimeField(default=None, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attacker',
            name='killID',
            field=models.ForeignKey(related_name=b'kills', to='analizer.kill'),
            preserve_default=True,
        ),
    ]

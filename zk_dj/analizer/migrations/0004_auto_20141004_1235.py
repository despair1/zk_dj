# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analizer', '0003_auto_20141002_1832'),
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
                ('securityStatus', models.FloatField()),
                ('weaponTypeID', models.IntegerField()),
                ('finalBlow', models.IntegerField()),
                ('shipTypeID', models.IntegerField()),
                ('corporationName', models.CharField(max_length=255)),
                ('characterName', models.CharField(max_length=255)),
                ('allianceName', models.CharField(max_length=255)),
                ('allianceID', models.ForeignKey(related_name=b'attackers', to='analizer.alli')),
                ('characterID', models.ForeignKey(related_name=b'attakers', to='analizer.pilot')),
                ('corporationID', models.ForeignKey(related_name=b'attackers', to='analizer.corp')),
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
                ('allianceID', models.ForeignKey(related_name=b'victim', to='analizer.alli')),
                ('characterID', models.ForeignKey(related_name=b'victim', to='analizer.pilot')),
                ('corporationID', models.ForeignKey(related_name=b'victim', to='analizer.corp')),
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
        migrations.AddField(
            model_name='corp',
            name='cached',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pilot',
            name='cached',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
    ]

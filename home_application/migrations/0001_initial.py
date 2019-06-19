# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostDisk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=64, verbose_name='\u4e3b\u673a\u540d')),
                ('ip', models.CharField(max_length=64, verbose_name='\u4e3b\u673aip')),
                ('os', models.CharField(max_length=64, verbose_name='\u7cfb\u7edf')),
                ('disk', models.CharField(max_length=64, verbose_name='\u78c1\u76d8\u5206\u533a')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65e5\u671f')),
            ],
            options={
                'db_table': 'host_disk',
            },
        ),
    ]

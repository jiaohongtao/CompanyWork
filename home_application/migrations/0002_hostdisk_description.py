# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostdisk',
            name='description',
            field=models.TextField(default=b'', max_length=100, verbose_name='\u63cf\u8ff0'),
        ),
    ]

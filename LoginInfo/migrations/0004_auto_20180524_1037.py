# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginInfo', '0003_auto_20180524_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=128),
        ),
    ]

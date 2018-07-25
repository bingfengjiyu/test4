# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginInfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='emial',
            field=models.CharField(default=None, max_length=128),
        ),
    ]

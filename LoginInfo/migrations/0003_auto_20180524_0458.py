# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginInfo', '0002_userinfo_emial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='emial',
            new_name='email',
        ),
    ]

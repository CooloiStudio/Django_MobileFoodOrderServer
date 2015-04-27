# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_ordermodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='deal',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='address',
            field=models.TextField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_foodmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='price',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]

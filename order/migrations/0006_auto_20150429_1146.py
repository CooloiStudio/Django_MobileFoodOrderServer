# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20150427_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketmodel',
            name='food',
            field=models.ForeignKey(to='order.FoodModel'),
        ),
    ]

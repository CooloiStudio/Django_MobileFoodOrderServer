# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasketModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('food', models.IntegerField(default=1)),
                ('order', models.ForeignKey(to='order.OrderModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='food',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='address',
            field=models.TextField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='confirm',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]

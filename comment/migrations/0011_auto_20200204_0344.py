# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-04 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_auto_20200204_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.TextField(blank=True, default=b'[{"content": "BigBox", "userImage": "Mall of America", "id": 1000, "author": "Mall of America"}]', max_length=4000, null=True, verbose_name='Yorum Ekle'),
        ),
    ]

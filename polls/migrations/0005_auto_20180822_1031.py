# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-22 10:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180822_1013'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='choice_text',
            new_name='comment_text',
        ),
    ]

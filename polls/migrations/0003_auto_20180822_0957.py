# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-22 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180822_0930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='choice_text',
            new_name='comment_text',
        ),
    ]

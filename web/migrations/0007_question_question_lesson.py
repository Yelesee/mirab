# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-22 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_lesson',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 08:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170621_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_password',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

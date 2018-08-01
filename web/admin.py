# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student,Mark,Study,SysMark,PracLevel,Question,Practice

# Register your models here.

admin.site.register(Student)
admin.site.register(Mark)
admin.site.register(Study)
admin.site.register(SysMark)
admin.site.register(PracLevel)
admin.site.register(Question)
admin.site.register(Practice)
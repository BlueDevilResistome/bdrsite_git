# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Agar, Site, Run, Swabber, Plate, Isolate

admin.site.register(Agar)
admin.site.register(Site)
admin.site.register(Run)
admin.site.register(Swabber)
admin.site.register(Plate)
admin.site.register(Isolate)
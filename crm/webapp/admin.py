from django.contrib import admin

# Register your models here.

from . models import *
#ReportSuspect, wantedSuspect

admin.site.register(Record)
admin.site.register(ReportSuspect)
#admin.site.register(wantedSuspect)

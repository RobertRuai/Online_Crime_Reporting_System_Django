from django.contrib import admin

# Register your models here.

from . models import *


#class CrimeReportAdmin(admin.ModelAdmin):
#    list_display = ('title', 'suspect_name',  'status', 'reported_by', 'created_at')
#    list_filter = ('status', 'created_at')
#    search_fields = ('title', 'suspect_name', 'description', 'reported_by__username')

#admin.site.register(CrimeReport, CrimeReportAdmin)
admin.site.register(Record)
admin.site.register(ReportSuspect)

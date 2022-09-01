from django.contrib import admin

# Register your models here.

from .models import Intern


class InternAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_name', 'job_title','status', 'started_time')
    list_filter = ('status','started_time')
    search_fields = ('company_name', 'postal')
    fieldsets = (
        (None, {
         'fields': (
                'started_time',
                 ('company_name', 'job_title', 'postal'),
                 'status', 
                 )
         }),
    )


admin.site.register(Intern, InternAdmin)
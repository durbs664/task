from django.contrib import admin

from .models import *

class SP_Admin(admin.ModelAdmin):
    list_display = ['name', 'panno', 'contactno', 'averageRating']



admin.site.register(Service_Provider, SP_Admin)

    # fieldsets = (
    #     ('Section 1', {
    #         'fields': ('family','location')
    #     }),
    # )

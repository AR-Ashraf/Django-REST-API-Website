from django.contrib import admin
from .models import ApiApp


# Register your models here.

class ApiAppAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital', 'population')
    search_fields = ('name', 'capital')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(ApiApp, ApiAppAdmin)

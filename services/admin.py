from django.contrib import admin
from .models import Service, Category

# admin.site.register(Service)
admin.site.register(Category)

class ServiceAdmin(admin.ModelAdmin):
    """
    Display only used fields.
    """
    fieldsets = (
        (None, {
           'fields': ('name', 'category', 'available', 'description',)
        }),
    )
admin.site.register(Service, ServiceAdmin)

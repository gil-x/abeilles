from django.contrib import admin
from .models import Basket

class BasketAdmin(admin.ModelAdmin):
    """
    Disallow creation of more than one instance in admin.
    """
    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True

admin.site.register(Basket, BasketAdmin)

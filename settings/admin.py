from django.contrib import admin
from .models import ContactEmail, NewsletterConfig, RecipientEmail, SocialLinks


class OneInstanceLimiter(admin.ModelAdmin):
    """
    Disallow creation of more than one instance in admin.
    """

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True

admin.site.register(ContactEmail, OneInstanceLimiter)

admin.site.register(NewsletterConfig, OneInstanceLimiter)

admin.site.register(SocialLinks, OneInstanceLimiter)

admin.site.register(RecipientEmail)

from django.contrib import admin
# from .models import (
#         Homepage,
#         PageAssociation, PageTeam, PageMissions, PageValues, PagePartners,
#         PageGarden, PageGardenProject, PageBasket,
#         PageServices, PageServicesPro, PageServicesInd,
#         PageJobhunt,
#     )
from .models import (
        Homepage,
        PageAssociation, PageMissions, PageTerritorialInfluence,
        PageGarden, PageGardenProject, PageBasket,
        PageServices, PageServicesPro, PageServicesInd,
        PageJobhunt,
    )
# admin.site.register(Category)
# admin.site.register(Page)
# admin.site.register(Homepage)
# admin.site.register(PageAssociation)

# class MyModelAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#            'fields': ('field1', 'field2', 'field3')
#         }),
#         ('Advanced options', {
#             'fields': ('field4', 'field5'),
#         }),
#     )



class OneInstanceLimiter(admin.ModelAdmin):
    """
    Disallow creation of more than one instance in admin.
    """

    def has_add_permission(self, request):
        if self.model.objects.count() > 0:
            return False
        else:
            return True


class PrettyFieldset(OneInstanceLimiter):
    fieldsets = (
        ('En-tête', {
           'fields': ('title', 'headline', 'featured_image')
        }),
        ('Corps', {
           'fields': ('body1', 'image1')
        }),
        (None, {
           'fields': ('body2', 'image2')
        }),
        (None, {
           'fields': ('body3', 'image3')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description',),
        }),
    )


class PrettyFieldsetPlus(OneInstanceLimiter):
    fieldsets = (
        ('En-tête', {
           'fields': ('title', 'headline', 'featured_image')
        }),
        ('Corps', {
           'fields': ('body1', 'image1')
        }),
        (None, {
           'fields': ('body2', 'image2')
        }),
        (None, {
           'fields': ('body3', 'image3')
        }),
        ('SEO', {
            # 'fields': ('meta_title', 'meta_description', 'slug'),
            'fields': ('meta_title', 'meta_description',),
        }),
        ('Témoignages', {
            'fields': ('testimony_title',
            'testimony1_image', 'testimony1_name', 'testimony1_text',
            'testimony2_image', 'testimony2_name', 'testimony2_text',
            'testimony3_image', 'testimony3_name', 'testimony3_text',
            ),
        }),
    )

class HomepageAdmin(OneInstanceLimiter):
    pass
admin.site.register(Homepage, HomepageAdmin)


class PageGardenAdmin(OneInstanceLimiter):
    pass
admin.site.register(PageGarden, PageGardenAdmin)


class PageGardenProjectAdmin(PrettyFieldset):
    pass
admin.site.register(PageGardenProject, PageGardenProjectAdmin)


class PageBasketAdmin(OneInstanceLimiter):
    fieldsets = (
        ('En-tête', {
           'fields': ('title', 'headline', 'featured_image')
        }),
        ('Corps', {
           'fields': ('body1', 'image1')
        }),
        (None, {
           'fields': ('body2', 'image2')
        }),
        (None, {
           'fields': ('body3', 'image3')
        }),
        (None, {
            'fields': ('body_extra', 'body_food'),
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description',),
        }),
    )
admin.site.register(PageBasket, PageBasketAdmin)


class PageAssociationAdmin(PrettyFieldset):
    pass
admin.site.register(PageAssociation, PageAssociationAdmin)


# class PageTeamAdmin(PrettyFieldset):
#     pass
# admin.site.register(PageTeam, PageTeamAdmin)

class PageTerritorialInfluenceAdmin(PrettyFieldset):
    pass
admin.site.register(PageTerritorialInfluence, PageTerritorialInfluenceAdmin)

class PageMissionsAdmin(PrettyFieldset):
    pass
admin.site.register(PageMissions, PageMissionsAdmin)


# class PageValuesAdmin(PrettyFieldset):
#     pass
# admin.site.register(PageValues, PageValuesAdmin)


# class PagePartnersAdmin(PrettyFieldset):
#     pass
# admin.site.register(PagePartners, PagePartnersAdmin)





class PageJobhuntAdmin(OneInstanceLimiter):
    fieldsets = (
        ('En-tête', {
           'fields': ('title', 'headline', 'featured_image')
        }),
        ('Corps', {
           'fields': ('body1', 'image1')
        }),
        (None, {
           'fields': ('body2', 'image2')
        }),
        (None, {
           'fields': ('body3', 'image3')
        }),
        (None, {
            'fields': ('body_extra', 'image_extra'),
        }),
        ('SEO', {
            # 'fields': ('meta_title', 'meta_description', 'slug'),
            'fields': ('meta_title', 'meta_description',),
        }),
        ('Témoignages', {
            'fields': ('testimony_title',
            'testimony1_image', 'testimony1_name', 'testimony1_text',
            'testimony2_image', 'testimony2_name', 'testimony2_text',
            'testimony3_image', 'testimony3_name', 'testimony3_text',
            ),
        }),
    )
admin.site.register(PageJobhunt, PageJobhuntAdmin)


# class PageServicesAdmin(PrettyFieldsetPlus):
#     pass
# admin.site.register(PageServices, PageServicesAdmin)


class PageServicesProAdmin(PrettyFieldsetPlus):
    pass
admin.site.register(PageServicesPro, PageServicesProAdmin)


class PageServicesIndAdmin(PrettyFieldsetPlus):
    pass
admin.site.register(PageServicesInd, PageServicesIndAdmin)

# from .models import Page, PageImage
 
# class PageImageAdmin(admin.StackedInline):
#     model = PageImage
 
# @admin.register(Page)
# class PageAdmin(admin.ModelAdmin):
#     inlines = [PageImageAdmin]
 
#     class Meta:
#        model = Page
 
# @admin.register(PageImage)
# class PageImageAdmin(admin.ModelAdmin):
#     pass
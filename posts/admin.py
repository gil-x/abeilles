from django.contrib import admin
from .models import Post

# admin.site.register(Category)
# admin.site.register(Post)


class PrettyFieldset(admin.ModelAdmin):
    fieldsets = (
        ('Article', {
        #    'fields': ('category', 'promoted', 'title', 'extract', 'body', 'image')
           'fields': ('promoted', 'title', 'extract', 'body', 'image')
        }),
        ('Pièces en téléchargement', {
           'fields': ('file1', 'file1_name', 'file2', 'file2_name')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'slug'),
        }),
    )

class PostAdmin(PrettyFieldset):
    pass
admin.site.register(Post, PostAdmin)
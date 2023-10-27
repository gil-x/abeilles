from django.contrib import admin
from django.urls import path, include, re_path
from abeilles.views import Sample

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Account
    path('accounts/', include('users.urls')),

    # Services
    path('services/', include('services.urls')),

    # Basket
    path('panier/', include('basket.urls')),

    # Posts
    path('actualites/', include('posts.urls')),

    # Pages
    path('', include('pages.urls')),

    # CK Editor
    path('ckeditor/', include('ckeditor_uploader.urls')),

    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

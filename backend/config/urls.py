from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path('users/', include('users.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('', include('products.urls')),
    path('', include('comments.urls')),
    path('', include('basket.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

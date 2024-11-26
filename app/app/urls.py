from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('problems.urls')),
    path("test/", include('testunit.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_title = "Coding for Machine"
admin.site.site_header = "CfM"
admin.site.index_title = "Cidng for Machine"
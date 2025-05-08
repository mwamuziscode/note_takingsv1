from django.contrib import admin
from django.urls import path, include
# from notes.views.views import custom_404_view  # Import your custom 404 view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path("ckeditor5/", include('django_ckeditor_5.urls')),
]

# handler404 = 'notes.views.views.custom_404_view'
urlpatterns += [
    path('norjiras/', include('norjiras.urls')),
]



# If we are currently in DEBUG mode, we want to add the following two specific URL patterns.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from marvel_site import settings

from marvel_heroes.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('marvel_heroes.urls')),
]

handler404 = pageNotFound

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
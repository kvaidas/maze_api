from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from api import urls as api_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls.urlpatterns)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

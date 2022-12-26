from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .settings import MEDIA_ROOT, MEDIA_URL

from .views import LandingPage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPage.as_view(), name='landing_page'),
    path('books/', include('book.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include('users.urls')),

]
if settings.DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from user.admin import advisor_site
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('club/', include('club.urls')),
    path('user/', include('user.urls')),
    path('advisor/admin/', advisor_site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

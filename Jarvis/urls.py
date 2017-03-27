from django.conf.urls import url, include
from django.contrib import admin
from Jarvis import settings


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^admin/', admin.site.urls),
        url(r'^', include('logsys.urls')),
        url(r'^logsys/', include('logsys.urls')),
        url(r'^user/', include('users.urls')),
        url(r'^homes/', include('homes.urls')),
    ]

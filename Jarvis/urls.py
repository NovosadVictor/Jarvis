from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('logsys.urls')),
    url(r'^logsys/', include('logsys.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^homes/', include('homes.urls')),
]

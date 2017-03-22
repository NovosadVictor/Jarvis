from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/insert_home/', views.insert_home, name='insert_home'),
    url(r'^user_page/(?P<pk>\d+)/', views.user_page_detail, name='user_page')
]


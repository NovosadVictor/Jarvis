from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<pk>\d+)/homes_page/(?P<home_id>\d+)/', views.home_page_detail, name='homes_page'),
    url(r'^(?P<home_id>\d+)/rooms_page/(?P<room_id>\d+)/', views.room_detail, name='rooms_page'),
    url(r'^(?P<home_id>\d+)/insert_room/', views.insert_room, name='insert_room'),
    url(r'^(?P<room_id>\d+)/insert_device/', views.insert_device, name='insert_device'),
    url(r'^(?P<device_id>\d+)/update_values/', views.update_values, name='update_values'),
]
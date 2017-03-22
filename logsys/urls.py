from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.main_page, name='main_page'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout/', views.user_logout, name='logout'),
    url(r'^registration/', views.user_registration, name='registration'),
]
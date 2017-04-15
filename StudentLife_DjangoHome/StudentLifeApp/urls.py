from django.conf.urls import patterns, url
from StudentLifeApp import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^profile', views.profile, name='profile'),
               url(r'^timetable', views.timetable, name='timetable'),
               url(r'^buildings', views.buildings, name='buildings'),
               url(r'^staff', views.staff, name='staff'),
               ]

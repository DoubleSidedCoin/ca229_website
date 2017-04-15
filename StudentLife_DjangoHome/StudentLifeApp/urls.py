from django.conf.urls import patterns, url
from StudentLifeApp import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^profile', views.profile, name='profile'),
               url(r'^timetable', views.timetable, name='timetable'),
               ]

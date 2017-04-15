from django.conf.urls import  url
from StudentLifeApp import views

urlpatterns = [
               url(r'^$', views.timetable, name='timetable'),
               url(r'^$', views.index, name='index'),
               ]

# chat/urls.py
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
    url('tasks/', views.tasks, name='tasks'),
    url('largeboard/', views.largeboard, name='largeboard'),
    url('largeboarddragon/', views.largeboarddragon, name='largeboarddragon'),
    url('tasksdragon/' , views.tasksdragon, name='tasksdragon'),
]


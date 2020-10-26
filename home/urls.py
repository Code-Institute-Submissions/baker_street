from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rooms', views.our_rooms, name='our_rooms'),
    path('contact', views.contact, name='contact'),
    path('leaderboards', views.leaderboards, name='leaderboards'),
]

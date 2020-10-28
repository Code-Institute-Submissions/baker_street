from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('bookings', views.bookings, name='bookings'),
]

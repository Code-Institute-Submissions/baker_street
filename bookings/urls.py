from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('book_a_room/<room_id>', views.book_a_room, name='book_a_room'),
]

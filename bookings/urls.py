from django.urls import path
from . import views

urlpatterns = [
    path('bookings', views.bookings, name='bookings'),
    path('bookings_watson', views.bookings_watson, name='bookings_watson'),
    path('bookings_pink', views.bookings_pink, name='bookings_pink'),
    path('bookings_moriarty', views.bookings_moriarty, name='bookings_moriarty'),  # noqa: E501
    path('bag', views.bag, name='bag'),
]

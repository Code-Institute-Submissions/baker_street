from django.shortcuts import render, get_object_or_404
from .models import Rooms
from .forms import Booking


def bookings(request):

    rooms = Rooms.objects.all()
    context = {
        'room_info': rooms,
    }
    return render(request, 'bookings/bookings.html', context)


def book_a_room(request, room_id):
    room = get_object_or_404(Rooms, pk=room_id)
    form = Booking()
    context = {
        'room_title': room.room_title,
        'room_image': room.room_image,
        'description': room.room_description,
        'form': form,
        'id': room.id,
    }
    return render(request, 'bookings/book_a_room.html', context)

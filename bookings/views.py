from django.shortcuts import render
from .models import Rooms


def bookings(request):

    rooms = Rooms.objects.all()
    print(rooms)
    context = {
        'rooms': rooms,
    }

    return render(request, 'bookings/bookings.html', context)


def bookings_watson(request):

    watson = Rooms.objects.filter(pk=1)
    print(watson)
    context = {
        'watson': watson,
    }

    return render(request, 'bookings/bookings_watson.html', context)


def bookings_pink(request):

    pink = Rooms.objects.filter(pk=2)

    context = {
        'pink': pink,
    }

    return render(request, 'bookings/bookings_pink.html', context)


def bookings_moriarty(request):

    moriarty = Rooms.objects.filter(pk=3)

    context = {
        'moriarty': moriarty,
    }

    return render(request, 'bookings/bookings_moriarty.html', context)

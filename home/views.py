from django.shortcuts import render
from .models import Leaderboards
from django.conf import settings


def index(request):
    return render(request, 'home/index.html')


def our_rooms(request):
    return render(request, 'home/rooms.html')


def contact(request):
    map_api = settings.GOOGLE_MAP_API
    context = {
        map_api: 'map_api'
    }
    return render(request, 'home/contact.html', context)


def leaderboards(request):
    leaderboards = Leaderboards.objects.all()

    context = {
        'leaderboards': leaderboards,
    }
    return render(request, 'home/leaderboards.html', context)

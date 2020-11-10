from django.shortcuts import render
from .models import Leaderboards


def index(request):
    return render(request, 'home/index.html')


def our_rooms(request):
    return render(request, 'home/rooms.html')


def contact(request):
    return render(request, 'home/contact.html')


def leaderboards(request):
    leaderboards = Leaderboards.objects.all()

    context = {
        'leaderboards': leaderboards,
    }
    return render(request, 'home/leaderboards.html', context)

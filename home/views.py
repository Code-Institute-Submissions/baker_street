from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def our_rooms(request):
    return render(request, 'home/rooms.html')


def contact(request):
    return render(request, 'home/contact.html')


def leaderboards(request):
    return render(request, 'home/leaderboards.html')

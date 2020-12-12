from django.shortcuts import render
from .forms import PersonalInfoOrder


def checkout(request):

    orderinfo = PersonalInfoOrder
    context = {
        'orderinfo': orderinfo
    }
    return render(request, 'checkout/checkout.html', context)

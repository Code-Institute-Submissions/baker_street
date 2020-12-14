from django.shortcuts import render
from .forms import PersonalInfoOrder


def checkout(request):

    orderinfo = PersonalInfoOrder
    context = {
        'orderinfo': orderinfo,
        'stripe_public_key': 'pk_test_51HyFP7JEsTpKioAIGAWyLYhF6xW4qYFPKVLiDAZewMG9Ilwt885rOkMwPKqRztFqD9fXj25uXG3nwRGn1dDkiD3O00w5kF0dK0',  # noqa: E501
        'client_secret': 'test client secret'
    }
    return render(request, 'checkout/checkout.html', context)

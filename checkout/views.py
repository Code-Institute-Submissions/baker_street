from django.shortcuts import render, redirect, reverse
from .forms import PersonalInfoOrder
from bag.contexts import bag_contents
from bookings.forms import Booking
from django.conf import settings
from django.contrib import messages
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    bag_items = request.session.get('bag_items', [])
    if not bag:
        messages.error(request, 'There is nothing in your cart. Please select a room to play')  # noqa:E501
        return redirect(reverse('rooms'))

    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        currency=settings.STRIPE_CURRENCY,
        amount=stripe_total
    )
    print(intent)
    form = Booking()
    orderinfo = PersonalInfoOrder
    context = {
        'orderinfo': orderinfo,
        'edit_form': form,
        'stripe_public_key': 'stripe_public_key',
        'client_secret': 'test client secret'
    }
    return render(request, 'checkout/checkout.html', context)


def payment(request):

    context = {
        'stripe_public_key': 'pk_test_51HyFP7JEsTpKioAIGAWyLYhF6xW4qYFPKVLiDAZewMG9Ilwt885rOkMwPKqRztFqD9fXj25uXG3nwRGn1dDkiD3O00w5kF0dK0',  # noqa: E501
        'client_secret': 'test client secret'
    }
    return render(request, 'checkout/payment.html', context)

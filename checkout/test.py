from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PersonalInfoOrder
from bag.contexts import bag_contents
from django.conf import settings
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your back")
        return redirect(reverse('our_rooms'))

    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    orderinfo = PersonalInfoOrder()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')
    context = {
        'orderinfo': orderinfo,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, 'checkout/checkout.html', context)

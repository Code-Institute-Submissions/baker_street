from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse  # noqa: E501
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import PersonalInfoOrder
from .models import Order_Personal_Info
from profiles.models import UserProfile
from bookings.models import Room_Booking
from bag.contexts import bag_contents
from django.conf import settings
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        orderinfo = PersonalInfoOrder(form_data)
        if orderinfo.is_valid():
            order = orderinfo.save()
            order.original_bag = json.dumps(bag)
            order.save()
            return redirect(reverse('checkout_success', args=[order.order_number]))  # noqa: E501

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag")
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


def checkout_success(request, order_number):
    order = get_object_or_404(Order_Personal_Info, order_number=order_number)  # noqa: E501
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()
    if 'bag' in request.session:
        del request.session['bag']
    context = {
        'order': order,
        'profile': profile
    }
    return render(request, 'checkout/checkout_success.html', context)

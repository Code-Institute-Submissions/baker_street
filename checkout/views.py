from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import PersonalInfoOrder
from .models import Order_Personal_Info
from bag.contexts import bag_contents
from django.conf import settings
import stripe


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
        print(form_data)
        orderinfo = PersonalInfoOrder(form_data)
        print(f"orderinfo is \n{orderinfo}")
        if orderinfo.is_valid():
            print("order form is valid")
            order = orderinfo.save()
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
    messages.success(request, f'Your order was successful. Your oder number is {order_number}. A confirmation email will be sent to {order.email}. We look forward to seeing you')  # noqa: E501

    if 'bag' in request.session:
        del request.session['bag']
    context = {
        'order': order,
    }
    return render(request, 'checkout/checkout_success.html', context)

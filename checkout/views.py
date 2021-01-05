from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import PersonalInfoOrder
from bag.contexts import bag_contents
from bookings.forms import Booking
from django.conf import settings
from django.contrib import messages
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
        order_info = PersonalInfoOrder(form_data)
        if order_info.is_valid():
            order_info.save()
            for item_id, booking_details in bag.items():
                room = get_object_or_404(Rooms, pk=item_id)
                num_of_players = booking_details['num_of_players']
                total += int(num_of_players) * 25
                request.session['total'] = total
                date = booking_details['date']
                time = booking_details['time']
                bag_items.append({
                    'item_id': item_id,
                    'room_title': room.room_title,
                    'num_of_players': num_of_players,
                    'date': date,
                    'time': time,
                    })

    else:
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
        'client_secret': 'intent.client_secret'
    }
    return render(request, 'checkout/checkout.html', context)

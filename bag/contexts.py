from bookings.models import Room_Booking
from django.shortcuts import get_object_or_404
from bookings.models import Rooms


def bag_contents(request):

    bag_items = []
    bag = request.session.get('bag', {})

    for item_id, booking_details in bag.items():
        room = get_object_or_404(Rooms, pk=item_id)
        num_of_players = booking_details['num_of_players']
        date = booking_details['date']
        time = booking_details['time']
        bag_items.append({
            'item_id': item_id,
            'room': room,
            'num_of_players': num_of_players,
            'date': date,
            'time': time,
            })
    context = {
        'bag_items': bag_items,
        'num_of_players': num_of_players,
        'date': date,
        'time': time,
    }
    return context

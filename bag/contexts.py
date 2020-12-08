from django.shortcuts import get_object_or_404
from bookings.models import Rooms


def bag_contents(request):

    bag_items = []
    num_of_players = 0
    date = 0
    time = 0
    bag = request.session.get('bag', {})

    for item_id, booking_details in bag.items():
        if isinstance(item_id, type(booking_details)):
            room = get_object_or_404(Rooms, pk=item_id)
            booking_details = num_of_players, date, time
            booking_details += item_id
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
        else:
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
        'room': room,
        'num_of_players': num_of_players,
        'date': date,
        'time': time,
    }
    return context

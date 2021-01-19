from django.shortcuts import get_object_or_404
from bookings.models import Rooms


def bag_contents(request):

    bag_items = []
    total = 0
    num_of_players = 0
    date = 0
    time = 0
    bag = request.session.get('bag', {})
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
    context = {
        'bag_items': bag_items,
        'num_of_players': num_of_players,
        'date': date,
        'time': time,
        'total': total,
    }
    return context

from bookings.models import Room_Booking
from django.shortcuts import get_object_or_404


def bag_contents(request):

    bag_items = []
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data,):
            booking = get_object_or_404(Room_Booking, pk=item_id)
            print(item_id)
            bag_items.append({
                'item_id': item_id,
                'booking': booking,
                # 'num_of_players': num_of_players,
                # 'date': date,
                # 'time': time,
            })
    context = {
        'bag_items': bag_items,
        # 'num_of_players': num_of_players,
        # 'date': date,
        # 'time': time,
    }
    return context

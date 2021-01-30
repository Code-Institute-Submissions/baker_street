from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from bookings.models import Rooms
import json


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    if len(orders) < 1:
        return render(request, 'profiles/profile.html')
    else:
        order = orders[0]
        order.original_bag = json.loads(order.original_bag)
        for item_id, booked_room in order.original_bag.items():
            room = get_object_or_404(Rooms, pk=item_id)
            num_of_players = booked_room['num_of_players']
            date = booked_room['date']
            time = booked_room['time']
        context = {
            'room_title': room.room_title,
            'num_of_players': num_of_players,
            'date': date,
            'time': time,
            'profile': profile,
            'orders': orders,
            'order': profile.orders.all(),
        }
        return render(request, 'profiles/profile.html', context)


# def order_history(request, order_number):
#     order = get_object_or_404(Room_Booking, order_number=order_number)

#     context = {
#         'order': order,
#         'from_profile': True,
#     }

#     return render(request, 'profiles/profile.html', context)

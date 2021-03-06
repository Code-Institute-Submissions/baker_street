from django.shortcuts import (
    render, HttpResponse, get_object_or_404, redirect, reverse
    )
from django.contrib import messages
from bookings.models import Rooms
from bookings.forms import Booking


def bag(request):
    form = Booking()
    context = {
        'edit_form': form
    }
    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    # booking = get_object_or_404(Rooms, pk=item_id)
    # getting the number of players, date and time from the posted form
    num_of_players = int(request.POST.get('num_of_players'))
    date = (request.POST.get('date'))
    time = (request.POST.get('time'))
    bag = request.session.get('bag', {})
    # creating a dictionary for the details for the bag
    booking_details = {'num_of_players': num_of_players, 'date': date, 'time': time}  # noqa: E501
    print(f"number of players: {num_of_players}")
    print(f"date in the format received {date}")
    print(f"time in the format received {time}")
    bag[item_id] = booking_details

    request.session['bag'] = bag
    return redirect(reverse('checkout'))


def delete_from_bag(request, item_id):

    try:
        room = get_object_or_404(Rooms, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, (f'Removed {room.room_title} from your bag'))
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

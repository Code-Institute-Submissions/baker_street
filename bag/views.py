from django.shortcuts import (
    render, HttpResponse, get_object_or_404, redirect, reverse
    )
from django.contrib import messages
from bookings.models import Rooms


def bag(request):
    return render(request, 'bag/bag.html')


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
    return redirect(reverse('bag'))


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


def edit_bag_item(request, item_id):
    room = get_object_or_404(Rooms, pk=item_id)
    num_of_players = int(request.POST.get('num_of_players'))
    date = int(request.POST.get('date'))
    time = int(request.POST.get('time'))

    bag = request.session.get('bag', {})
    messages.success(request, (f'Removed {room.room_title} from your bag'))
    request.session['bag'] = bag
    return HttpResponse(status=200)


# def adjust_bag(request, item_id):
#     product = get_object_or_404(Product, pk=item_id)
#     quantity = int(request.POST.get('quantity'))
#     size = None
#     if 'product_size' in request.POST:
#         size = request.POST['product_size']
#     bag = request.session.get('bag', {})

#     if size:
#         if quantity > 0:
#             bag[item_id]['items_by_size'][size] = quantity
#             messages.success(request,
#                              (f'Updated size {size.upper()} '
#                               f'{product.name} quantity to '
#                               f'{bag[item_id]["items_by_size"][size]}'))
#         else:
#             del bag[item_id]['items_by_size'][size]
#             if not bag[item_id]['items_by_size']:
#                 bag.pop(item_id)
#             messages.success(request,
#                              (f'Removed size {size.upper()} '
#                               f'{product.name} from your bag'))
#     else:
#         if quantity > 0:
#             bag[item_id] = quantity
#             messages.success(request,
#                              (f'Updated {product.name} '
#                               f'quantity to {bag[item_id]}'))
#         else:
#             bag.pop(item_id)
#             messages.success(request,
#                              (f'Removed {product.name} '
#                               f'from your bag'))

#     request.session['bag'] = bag
#     return redirect(reverse('view_bag'))

from django.shortcuts import render, get_object_or_404


def bag(request):
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    booking = get_object_or_404(Booking, pk=item_id)
    players = int(request.POST.get('num_of_players'))
    bag = request.session.get('bag', {})
    bag[item_id]
    request.session['bag'] = bag
    return render(request, 'bag/bag.html')



def bag_contents(request):

    bag_items = []
    total = 0
    room_name = 0
    number_of_players = 0
    date = 0
    time = 0
    context = {
        'bag_items': bag_items,
        'total': total,
        'room_name': room_name,
        'number_of_players': number_of_players,
        'date': date,
        'time': time,
    }

    return context

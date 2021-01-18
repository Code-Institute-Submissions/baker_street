from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    context = {
        'profile': profile,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)



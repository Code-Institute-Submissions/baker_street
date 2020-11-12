from django import forms
from .models import Room_Booking


class Booking(forms.ModelForm):
    class Meta:
        model = Room_Booking
        fields = ['num_of_players', 'date', 'time']

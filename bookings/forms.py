from django import forms
from .models import Room_Booking


class ViewCalendar(forms.DateInput):
    input_type = 'date'


class Booking(forms.ModelForm):
    class Meta:
        model = Room_Booking
        fields = ['num_of_players', 'date', 'time']
        widgets = {'date': ViewCalendar()}

from django import forms
from .models import Room_Booking
from datetime import datetime


class ViewCalendar(forms.DateInput):
    input_type = 'date'


today = datetime.today().strftime('%Y-%m-%d')


class Booking(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Booking, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['min'] = today

    class Meta:
        model = Room_Booking
        fields = ['num_of_players', 'date', 'time']
        widgets = {'date': ViewCalendar()}

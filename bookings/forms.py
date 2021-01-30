from django import forms
from .models import Room_Booking
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ViewCalendar(forms.DateInput):
    input_type = 'date'


class Booking(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Booking, self).__init__(*args, **kwargs)
        date_now = datetime.now().date()
        start_date = date_now + relativedelta(days=+1)
        self.fields['date'].widget.attrs['min'] = start_date

    class Meta:
        model = Room_Booking
        fields = ['num_of_players', 'date', 'time']
        widgets = {'date': ViewCalendar()}

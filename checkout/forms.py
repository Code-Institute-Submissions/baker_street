from django import forms
from .models import Order_Personal_Info


class PersonalInfoOrder(forms.ModelForm):
    class Meta:
        model = Order_Personal_Info
        fields = ['full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'county', 'postcode',
                  'country', 'order_total']

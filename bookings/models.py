from django.db import models
from django.core.exceptions import ValidationError
import datetime
from checkout.models import Order_Personal_Info


class Rooms(models.Model):

    class Meta:
        verbose_name_plural = 'Rooms'

    room_title = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)  # noqa:E501
    room_description = models.CharField(max_length=254, null=False, blank=False)  # noqa:E501
    room_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return super().__str__()


def min_date(date):
    if date < datetime.now().date():
        raise ValidationError("Date cannot be in the past")


class Room_Booking(models.Model):
    NUM_PLAYERS = (
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )
    num_of_players = models.CharField(max_length=2, choices=NUM_PLAYERS)
    date = models.DateField(blank=False, null=False, validators=[min_date])
    TIME_OPTIONS = (
        (1000, '1000'),
        (1130, '1130'),
        (1300, '1300'),
        (1430, '1430'),
        (1600, '1600'),
        (1730, '1730'),
        (1900, '1900'),
        (2030, '2030'),
        (2200, '2200'),
    )
    time = models.TimeField(blank=False, null=False, choices=TIME_OPTIONS)
    order = models.ForeignKey(Order_Personal_Info, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')  # noqa: E501

    def __str__(self):
        return super().__str__()

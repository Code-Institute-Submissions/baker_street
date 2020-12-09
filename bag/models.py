from django.db import models


class Edit_Booking(models.Model):
    NUM_PLAYERS = (
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )
    num_of_players = models.CharField(max_length=2, choices=NUM_PLAYERS)
    date = models.DateField(blank=False, null=False)
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

    def __str__(self):
        return super().__str__()

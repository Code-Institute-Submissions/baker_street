from django.db import models


class Rooms(models.Model):

    class Meta:
        verbose_name_plural = 'Rooms'

    room_title = models.CharField(max_length=254, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)  # noqa:E501
    room_description = models.CharField(max_length=254, null=False, blank=False)  # noqa:E501
    room_image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return super().__str__()

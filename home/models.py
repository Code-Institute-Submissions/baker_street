from django.db import models


class Leaderboards(models.Model):

    class Meta:
        verbose_name_plural = 'Leaderboards'

    room_name = models.CharField(max_length=254, null=False, blank=False)
    team_1_name = models.CharField(max_length=254, null=False, blank=False)
    team_2_name = models.CharField(max_length=254, null=False, blank=False)
    team_3_name = models.CharField(max_length=254, null=False, blank=False)
    team_1_time = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)  # noqa:E501
    team_2_time = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)  # noqa:E501
    team_3_time = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)  # noqa:E501

    def __str__(self):
        return super().__str__()

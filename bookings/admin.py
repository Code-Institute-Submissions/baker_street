from django.contrib import admin
from .models import Rooms


class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        'room_title',
    )

    ordering = ('pk',)


admin.site.register(Rooms, RoomsAdmin)

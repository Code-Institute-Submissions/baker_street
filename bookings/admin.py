from django.contrib import admin
from .models import Rooms, Room_Booking


class RoomsAdmin(admin.ModelAdmin):
    list_display = (
        'room_title',
    )

    ordering = ('pk',)


class RoomBookingAdmin(admin.ModelAdmin):
    list_display = (
    )


admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Room_Booking, RoomBookingAdmin)

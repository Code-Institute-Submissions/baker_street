from django.contrib import admin
from .models import Order_Personal_Info


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'date',
                       'order_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county',
              'order_total',)

    ordering = ('-date',)


admin.site.register(Order_Personal_Info, OrderAdmin)

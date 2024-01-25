from django.contrib import admin

from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'price_usd', 'username', 'phone_number', 'datatime_found')
    list_filter = (
        'title', 'price_usd', 'odometer', 'username', 'phone_number', 'image_url', 'images_count', 'car_number',
        'car_vin', 'datatime_found')
    search_fields = (
        'url', 'title', 'price_usd', 'odometer', 'username', 'phone_number', 'image_url', 'images_count', 'car_number',
        'car_vin', 'datatime_found')
    ordering = (
        'title', 'price_usd', 'odometer', 'username', 'phone_number', 'image_url', 'images_count', 'car_number',
        'car_vin', 'datatime_found')
    readonly_fields = ('datatime_found',)

    fieldsets = (
        (None, {
            'fields': ('url', 'title', 'price_usd', 'odometer', 'username', 'phone_number', 'image_url', 'images_count',
                       'car_number', 'car_vin', 'datatime_found')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('url', 'title', 'price_usd', 'odometer', 'username', 'phone_number', 'image_url', 'images_count',
                       'car_number', 'car_vin', 'datatime_found')
        }),
    )

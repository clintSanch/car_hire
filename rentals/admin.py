from django.contrib import admin
from .models import Car, Customer, Rental, Booking

# Register Car model
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'model', 'availability')
    search_fields = ('license_plate', 'model')
    list_filter = ('availability',)

# Register Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

# Register Rental model
@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('car', 'customer', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('customer__name', 'car__model')

# Register Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'car', 'pickup_date', 'return_date', 'booking_date')
    list_filter = ('pickup_date', 'return_date')
    search_fields = ('customer_name', 'car__model')

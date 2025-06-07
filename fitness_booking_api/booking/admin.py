from django.contrib import admin
from .models import FitnessClass, Booking
# Register your models here.

class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'instructor', 'available_slots']

class BookingClassAdmin(admin.ModelAdmin):
    list_display = ("fitness_class", "client_name", "client_email")



admin.site.register(FitnessClass, FitnessClassAdmin)
admin.site.register(Booking, BookingClassAdmin)

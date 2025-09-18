from django.contrib import admin
from .models import DriverInfo

@admin.register(DriverInfo)
class DriverInfoAdmin(admin.ModelAdmin):
    list_display = ('driverName', 'vehicleId', 'date', 'location')
    search_fields = ('driverName', 'vehicleId', 'location')
    list_filter = ('date',)
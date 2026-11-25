from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdminPerso(admin.ModelAdmin):
    list_display = (
        'id', 'reason', 'status',
        'duration_minutes', 'appointment_date',
        'doctor', 'patient',
    )
    #Filter accepts double fields (add comma for one field filter)
    list_filter = ('status',) 
    #search_fields = ('duration_minutes', 'doctor_username')
    fieldsets = (
        ('Appointment Information', {
        'fields': ('reason', 'status')
        }),
        ('Appointment Details', {
        'fields': ('duration_minutes',
        'appointment_date', 'doctor', 'patient')
        }),
        ('Non Editable', {
        'fields': ('created_at', 'updated_at')
        }),
        )
    readonly_fields = ('created_at', 'updated_at')




from django.contrib import admin
from .models import Slot

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id', 'slot_name', 'status', 'created_time')
    list_filter = ('status',)
    search_fields = ('slot_name',)
    ordering = ('created_time',)

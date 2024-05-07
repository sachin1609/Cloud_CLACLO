from django.contrib import admin
from .models import University

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'activation_date', 'deactivation_date']

    def has_change_permission(self, request, obj=None):
        # Custom permission logic can go here
        return super().has_change_permission(request, obj)

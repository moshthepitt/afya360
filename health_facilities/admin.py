from django.contrib import admin

from .models import HealthFacility, FacilityOwner, FacilityType


class HealthFacilityAdmin(admin.ModelAdmin):
    search_fields = ['name', 'facility_code']
    list_filter = ['level', 'facility_class', 'facility_type', 'owner', 'province', 'county', 'status']
    list_display = ['name', 'facility_code']


class FacilityOwnerAdmin(admin.ModelAdmin):
    search_fields = ['name']


class FacilityTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(HealthFacility, HealthFacilityAdmin)
admin.site.register(FacilityOwner, FacilityOwnerAdmin)
admin.site.register(FacilityType, FacilityTypeAdmin)

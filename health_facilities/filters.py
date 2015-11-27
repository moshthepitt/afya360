import django_filters

from .models import HealthFacility


class HealthFacilityFilter(django_filters.FilterSet):

    class Meta:
        model = HealthFacility
        fields = [
            'county',
            'province',
            'district',
            'division',
            'location',
            'sub_location',
            'constituency',
            'owner',
            'facility_type',
            'agency',
            'status',
            'level',
            'facility_class',
        ]

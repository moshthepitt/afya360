from rest_framework import permissions, viewsets, filters

from .models import HealthFacility
from .serializers import HealthFacilitySerializer
from .filters import HealthFacilityFilter


class HealthFacilityViewSet(viewsets.ModelViewSet):
    queryset = HealthFacility.objects.order_by('name')
    serializer_class = HealthFacilitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = HealthFacilityFilter
    ordering_fields = ('name')

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

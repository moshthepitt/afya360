from rest_framework import permissions, viewsets

from .models import HealthFacility
from .serializers import HealthFacilitySerializer


class HealthFacilityViewSet(viewsets.ModelViewSet):
    queryset = HealthFacility.objects.order_by('name')
    serializer_class = HealthFacilitySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

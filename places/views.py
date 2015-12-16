from rest_framework import permissions, viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Province, County, District, Division
from .models import Constituency, Location, SubLocation

from .serializers import ProvinceSerializer, ConstituencySerializer, CountySerializer
from .serializers import DistrictSerializer, DivisionSerializer, LocationSerializer
from .serializers import SubLocationSerializer


class ProvinceViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Province.objects.order_by('name')
    serializer_class = ProvinceSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class CountyViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = County.objects.order_by('name')
    serializer_class = CountySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class DistrictViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = District.objects.order_by('name')
    serializer_class = DistrictSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class DivisionViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Division.objects.order_by('name')
    serializer_class = DivisionSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class LocationViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Location.objects.order_by('name')
    serializer_class = LocationSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class SubLocationViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = SubLocation.objects.order_by('name')
    serializer_class = SubLocationSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class ConstituencyViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = Constituency.objects.order_by('name')
    serializer_class = ConstituencySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

from rest_framework import permissions, viewsets

from .models import Province, County, District, Division
from .models import Constituency, Location, SubLocation

from .serializers import ProvinceSerializer, ConstituencySerializer, CountySerializer
from .serializers import DistrictSerializer, DivisionSerializer, LocationSerializer
from .serializers import SubLocationSerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.order_by('name')
    serializer_class = ProvinceSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class CountyViewSet(viewsets.ModelViewSet):
    queryset = County.objects.order_by('name')
    serializer_class = CountySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.order_by('name')
    serializer_class = DistrictSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.order_by('name')
    serializer_class = DivisionSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.order_by('name')
    serializer_class = LocationSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class SubLocationViewSet(viewsets.ModelViewSet):
    queryset = SubLocation.objects.order_by('name')
    serializer_class = SubLocationSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class ConstituencyViewSet(viewsets.ModelViewSet):
    queryset = Constituency.objects.order_by('name')
    serializer_class = ConstituencySerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

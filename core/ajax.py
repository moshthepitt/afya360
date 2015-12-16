from rest_framework.views import APIView
from rest_framework.response import Response

from health_facilities.models import HealthFacility
from health_facilities.serializers import HealthFacilitySerializer

from places.models import County, Constituency
from places.serializers import ConstituencySerializer, CountySerializer

from .mixins import CachePageMixin


class HomeResources(CachePageMixin, APIView):

    def get(self, request, format=None):
        """
        Return a list of home page resources
        """
        data = {}
        facilities = HealthFacility.objects.order_by('?')[:8]
        facilities = [HealthFacilitySerializer(x).data for x in facilities]
        counties = County.objects.all()
        constituencies = Constituency.objects.all()
        counties = [CountySerializer(x).data for x in counties]
        constituencies = [ConstituencySerializer(x).data for x in constituencies]
        data['facilities'] = facilities
        data['counties'] = counties
        data['constituencies'] = constituencies
        return Response(data)

from django.views.generic.detail import DetailView

from rest_framework import permissions, viewsets
from drf_haystack.viewsets import HaystackViewSet
from django_filters.rest_framework import DjangoFilterBackend

from health_facilities.models import HealthFacility
from health_facilities.serializers import HealthFacilitySerializer
from health_facilities.serializers import HealthFacilitySearchSerializer
from health_facilities.filters import HealthFacilityFilter


class HealthFacilityViewSet(viewsets.ModelViewSet):
    queryset = HealthFacility.objects.order_by('name')
    serializer_class = HealthFacilitySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = HealthFacilityFilter
    ordering_fields = ('name')

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)


class HealthFacilitySearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to
    # include
    # in the search result. You might have several models indexed, and this
    # provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the
    # scenes.
    index_models = [HealthFacility]

    serializer_class = HealthFacilitySearchSerializer


class HealthFacilityView(DetailView):

    model = HealthFacility
    template_name = "health_facilities/health_facility.html"

    def get_context_data(self, **kwargs):
        context = super(HealthFacilityView, self).get_context_data(**kwargs)
        return context

from django.views.generic.base import TemplateView

from health_facilities.models import HealthFacility

from places.models import County, Constituency


class AngularView(TemplateView):

    template_name = "angular/home.html"


class HomePage(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        facilities = HealthFacility.objects.exclude(
            twenty_four_hour=False).exclude(
            location_description="").exclude(nearest_town='').order_by('?')[:8]
        counties = County.objects.all()
        constituencies = Constituency.objects.all()
        context['facilities'] = facilities
        context['counties'] = counties
        context['constituencies'] = constituencies
        return context

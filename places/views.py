from django.views.generic.detail import DetailView

from django.core.paginator import Paginator, PageNotAnInteger


class PlaceView(DetailView):

    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(PlaceView, self).get_context_data(**kwargs)
        objects = self.object.healthfacility_set.active()

        try:
            page = self.request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        paginator = Paginator(objects, 25)
        facilities = paginator.get_page(page)

        context['facilities'] = facilities
        return context

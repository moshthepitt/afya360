from django.views.generic.detail import DetailView


class PlaceView(DetailView):

    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super(PlaceView, self).get_context_data(**kwargs)
        context['facilities'] = self.object.healthfacility_set.active()
        return context

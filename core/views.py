from django.views.generic.base import TemplateView

from .mixins import CachePageMixin


class HomePageView(CachePageMixin, TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context

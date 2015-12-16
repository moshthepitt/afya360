from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CachePageMixin(object):

    @method_decorator(cache_page(60 * 60 * 6))
    def dispatch(self, *args, **kwargs):
        return super(CachePageMixin, self).dispatch(*args, **kwargs)

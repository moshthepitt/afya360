from django.contrib.sitemaps import Sitemap, GenericSitemap
from django.core.paginator import Paginator

from .models import HealthFacility


class HealthFacilitySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return HealthFacility.objects.all()

    def lastmod(self, obj):
        return obj.updated_on


def health_facility_sitemaps(chunk=1000):
    """
    next we'll attemtp to generate a number of sitemaps in chunks using Paginator and GenericSitemap
    """
    health_facility_sitemap = {}
    health_facilities = HealthFacility.objects.all()
    paginated_health_facilities = Paginator(health_facilities, chunk)
    for this_page in paginated_health_facilities.page_range:
        health_facility_dict = {
            'queryset': paginated_health_facilities.page(this_page).object_list,
            'date_field': 'updated_on',
        }
        health_facility_sitemap['health_facilitys_%s' % this_page] = GenericSitemap(
            health_facility_dict, priority=0.6, changefreq='monthly')
    return health_facility_sitemap

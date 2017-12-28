from django.contrib.sitemaps import GenericSitemap

from health_facilities.sitemaps import health_facility_sitemaps

from places.models import Province, County, District, Division, Location
from places.models import SubLocation
from places.models import Constituency

province_dict = {
    'queryset': Province.objects.all(),
    'date_field': 'updated_on',
}

county_dict = {
    'queryset': County.objects.all(),
    'date_field': 'updated_on',
}

district_dict = {
    'queryset': District.objects.all(),
    'date_field': 'updated_on',
}

division_dict = {
    'queryset': Division.objects.all(),
    'date_field': 'updated_on',
}

location_dict = {
    'queryset': Location.objects.all(),
    'date_field': 'updated_on',
}

sub_location_dict = {
    'queryset': SubLocation.objects.all(),
    'date_field': 'updated_on',
}

constituency_dict = {
    'queryset': Constituency.objects.all(),
    'date_field': 'updated_on',
}

sitemaps = {
    'province': GenericSitemap(province_dict, priority=0.6,
                               changefreq='monthly'),
    'county': GenericSitemap(county_dict, priority=0.6, changefreq='monthly'),
    'district': GenericSitemap(district_dict, priority=0.6,
                               changefreq='monthly'),
    'division': GenericSitemap(division_dict, priority=0.6,
                               changefreq='monthly'),
    'location': GenericSitemap(location_dict, priority=0.6,
                               changefreq='monthly'),
    'sub_location': GenericSitemap(sub_location_dict, priority=0.6,
                                   changefreq='monthly'),
    'constituency': GenericSitemap(constituency_dict, priority=0.6,
                                   changefreq='monthly'),
}

sitemaps = sitemaps.copy()
sitemaps.update(health_facility_sitemaps())

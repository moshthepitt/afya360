from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from core.views import AngularView, HomePage
from core.ajax import AngularResources

from core.sitemaps import sitemaps

from places.viewsets import ProvinceViewSet, CountyViewSet, ConstituencyViewSet
from places.viewsets import DistrictViewSet, DivisionViewSet, LocationViewSet
from places.viewsets import SubLocationViewSet
from health_facilities.views import HealthFacilityViewSet, HealthFacilityView
from health_facilities.views import HealthFacilitySearchView

router = routers.SimpleRouter()
router.register(r'provinces', ProvinceViewSet)
router.register(r'counties', CountyViewSet)
router.register(r'constituencies', ConstituencyViewSet)
router.register(r'divisions', DivisionViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'sub-locations', SubLocationViewSet)
router.register(r'health-facilities', HealthFacilityViewSet)
router.register(r'hf-search', HealthFacilitySearchView,
                base_name="health-facilities-search")

sitemap_urls = [
    url(r'^sitemap\.xml$', 'fastsitemaps.views.index', {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', 'fastsitemaps.views.sitemap',
        {'sitemaps': sitemaps}),
]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/home-resources/$', AngularResources.as_view(),
        name="home_resources"),
    url(r'^api/v1/', include(router.urls)),
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^page/', include('django.contrib.flatpages.urls')),

    url(r'^new/$', HomePage.as_view(), name='home'),
    url(r'^new/health-facility/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        HealthFacilityView.as_view(),
        name='health_facility'),
    url(r'^new/place/', include('places.urls', namespace='places')),

    url(r'^.*$', AngularView.as_view(), name='ng_home'),
]

urlpatterns = sitemap_urls + urlpatterns

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT})
    ]

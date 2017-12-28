from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from core.views import AngularView, HomePage
from core.ajax import AngularResources
from fastsitemaps.views import index as fastsitemaps_index
from fastsitemaps.views import sitemap as fastsitemaps_sitemap

from core.sitemaps import sitemaps

from places.viewsets import ProvinceViewSet, CountyViewSet, ConstituencyViewSet
from places.viewsets import DistrictViewSet, DivisionViewSet, LocationViewSet
from places.viewsets import SubLocationViewSet
from places import urls as places_urls
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
    url(r'^sitemap\.xml$', fastsitemaps_index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', fastsitemaps_sitemap,
        {'sitemaps': sitemaps}),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/home-resources/$', AngularResources.as_view(),
        name="home_resources"),
    url(r'^api/v1/', include((router.urls, 'apiv1'), namespace='apiv1')),

    url(r'^new/$', HomePage.as_view(), name='home'),
    url(r'^new/health-facility/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        HealthFacilityView.as_view(),
        name='health_facility'),
    url(r'^new/place/', include((places_urls, 'places'), namespace='places')),

    url(r'^.*$', AngularView.as_view(), name='ng_home'),
]

urlpatterns = sitemap_urls + urlpatterns

if settings.DEBUG:
    from django.views.static import serve  # noqa
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]

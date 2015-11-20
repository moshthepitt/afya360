from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

from rest_framework import routers

from core.views import HomePageView
from places.views import ProvinceViewSet, CountyViewSet, ConstituencyViewSet
from places.views import DistrictViewSet, DivisionViewSet, LocationViewSet
from places.views import SubLocationViewSet
from health_facilities.views import HealthFacilityViewSet

router = routers.SimpleRouter()
router.register(r'provinces', ProvinceViewSet)
router.register(r'counties', CountyViewSet)
router.register(r'constituencies', ConstituencyViewSet)
router.register(r'divisions', DivisionViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'sub-locations', SubLocationViewSet)
router.register(r'health-facilities', HealthFacilityViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(router.urls)),
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^page/', include('django.contrib.flatpages.urls')),

    url(r'^$', HomePageView.as_view(), name='home'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    ]

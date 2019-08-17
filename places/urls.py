from django.conf.urls import url

from places.models import County, Constituency, Province, District
from places.models import Location, Division, SubLocation
from places.views import PlaceView

urlpatterns = [
    url(r'^county/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        PlaceView.as_view(model=County),
        name='county'),
    url(r'^constituency/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        PlaceView.as_view(model=Constituency),
        name='constituency'),
    url(r'^province/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        PlaceView.as_view(model=Province),
        name='province'),
    url(r'^district/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        PlaceView.as_view(model=District),
        name='district'),
    url(r'^location/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        PlaceView.as_view(model=Location),
        name='location'),
    url(r'^division/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        PlaceView.as_view(model=Division),
        name='division'),
    url(r'^sub_location/(?P<slug>[-\w]+)/(?P<pk>\d+)/$',
        PlaceView.as_view(model=SubLocation),
        name='sub_location'),
]

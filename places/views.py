from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404

from places.models import Province, County, District, Division
from places.models import Constituency, Location, SubLocation

# -*- coding: utf-8 -*-
from haystack import indexes

from .models import HealthFacility


class HealthFacilityIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name')
    slug = indexes.CharField(model_attr='slug')
    id = indexes.IntegerField(model_attr='id', faceted=True)
    county = indexes.IntegerField(model_attr='county__id', faceted=True)
    province = indexes.IntegerField(model_attr='province__id', null=True, faceted=True)
    district = indexes.IntegerField(model_attr='district__id', null=True, faceted=True)
    division = indexes.IntegerField(model_attr='division__id', null=True, faceted=True)
    location = indexes.IntegerField(model_attr='location__id', null=True, faceted=True)
    sub_location = indexes.IntegerField(model_attr='sub_location__id', null=True, faceted=True)
    constituency = indexes.IntegerField(model_attr='constituency__id', null=True, faceted=True)
    facility_type = indexes.IntegerField(model_attr='facility_type__id', null=True, faceted=True)
    owner = indexes.IntegerField(model_attr='owner__id', faceted=True)
    level = indexes.IntegerField(model_attr='level', faceted=True)
    agency = indexes.IntegerField(model_attr='agency', faceted=True)
    status = indexes.IntegerField(model_attr='status', faceted=True)
    rendered = indexes.CharField(use_template=True, indexed=False)
    # rating = indexes.DecimalField(model_attr='average_rating', null=True, faceted=True)
    # reviews = indexes.IntegerField(model_attr='review_count')

    # def prepare_rating(self, obj):
    #     return None if not obj.average_rating else obj.average_rating

    def prepare_id(self, obj):
        return obj.pk

    def get_model(self):
        return HealthFacility

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.active()

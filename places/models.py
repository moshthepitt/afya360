from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from autoslug import AutoSlugField


@python_2_unicode_compatible
class PlaceModel(models.Model):

    """
    An abstract model for common place fields
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    name = models.CharField(_("Name"), max_length=255, blank=False)

    def meta(self):
        return self._meta

    def model_name(self):
        return self.meta().verbose_name

    def facility_count(self):
        return self.healthfacility_set.all().count()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Province(PlaceModel):
    slug = AutoSlugField(populate_from='name', unique=True)

    def get_absolute_url(self):
        return "/place/province/{0}/{1}/".format(self.slug, self.pk)

    class Meta:
        ordering = ['name']
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')


class County(PlaceModel):
    slug = AutoSlugField(populate_from='name', unique=True)

    def get_absolute_url(self):
        return "/place/county/{0}/{1}/".format(self.slug, self.pk)

    class Meta:
        ordering = ['name']
        verbose_name = _('County')
        verbose_name_plural = _('Counties')


class District(PlaceModel):
    province = models.ForeignKey(Province, verbose_name=_("Province"),
                                 on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from='name', unique_with='province__name')

    def get_absolute_url(self):
        return "/place/district/{0}/{1}/".format(self.slug, self.pk)

    class Meta:
        ordering = ['name']
        verbose_name = _('District')
        verbose_name_plural = _('Districts')


class Division(PlaceModel):
    district = models.ForeignKey(District, verbose_name=_("District"),
                                 on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from='name', unique_with='district__name')

    def get_absolute_url(self):
        return "/place/division/{0}/{1}/".format(self.slug, self.pk)

    class Meta:
        ordering = ['name']
        verbose_name = _('Division')
        verbose_name_plural = _('Divisions')


class Location(PlaceModel):
    division = models.ForeignKey(Division, verbose_name=_("Division"),
                                 on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from='name', unique_with='division__name')

    def get_absolute_url(self):
        return "/place/location/{0}/{1}/".format(self.slug, self.pk)

    class Meta:
        ordering = ['name']
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')


class SubLocation(PlaceModel):
    location = models.ForeignKey(Location, verbose_name=_("Location"),
                                 on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from='name', unique_with='location__name')

    def get_absolute_url(self):
        return "/place/sub_location/{0}/{1}/".format(self.slug, self.pk)

    class Meta:
        ordering = ['name']
        verbose_name = _('Sub Location')
        verbose_name_plural = _('Sub Locations')


class Constituency(PlaceModel):
    county = models.ForeignKey(County, verbose_name=_("County"),
                               on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from='name', unique_with='county__name')

    def get_absolute_url(self):
        return "/place/constituency/{0}/{1}/".format(self.slug, self.pk)

    class Meta:
        ordering = ['name']
        verbose_name = _('Constituency')
        verbose_name_plural = _('Constituencies')

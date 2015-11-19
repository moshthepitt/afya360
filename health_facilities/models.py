from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.geos import Point

from autoslug import AutoSlugField
from phonenumber_field.modelfields import PhoneNumberField

from places.models import County, Constituency, Province, District
from places.models import Division, Location, SubLocation


class GeoFacilityManager(models.GeoManager):
    pass


@python_2_unicode_compatible
class HealthFacility(models.Model):

    """
    This model stores info. abut health facilities
    """

    NGO = 996
    OTHER = 997
    NA = 998
    UNKOWN = 999

    LEVEL1 = 1
    LEVEL2 = 2
    LEVEL3 = 3
    LEVEL4 = 4
    LEVEL5 = 5
    LEVEL6 = 6

    LEVEL_CHOICES = [
        (LEVEL1, _("Level 1")),
        (LEVEL2, _("Level 2")),
        (LEVEL3, _("Level 3")),
        (LEVEL4, _("Level 4")),
        (LEVEL5, _("Level 5")),
        (LEVEL6, _("Level 6")),
        (UNKOWN, _("Not Classified")),
    ]

    BLOOD_BANK = 1
    DENTAL_CLINIC = 2
    DISPENSARY = 3
    DISTRICT_HEALTH_OFFICE = 4
    DISTRICT_HOSPITAL = 5
    EYE_CENTRE = 6
    EYE_CLINIC = 7
    HEALTH_CENTRE = 8
    HEALTH_PROGRAMME = 9
    HEALTH_PROJECT = 10
    LABORATORY = 11
    MATERNITY_HOME = 12
    MEDICAL_CENTRE = 13
    MEDICAL_CLINIC = 14
    MEDICAL_CLINIC = 15
    NURSING_HOME = 16
    OTHER_HOSPITAL = 18
    PROVINCIAL_GENERAL_HOSPITAL = 19
    RADIOLOGY_UNIT = 20
    SUB_DISTRICT_HOSPITAL = 21
    TRAINING_INSTITUTION_IN_HEALTH = 22
    VCT_CENTRE = 23

    TYPE_CHOICES = [
        (BLOOD_BANK, _('Blood Bank')),
        (DENTAL_CLINIC, _('Dental Clinic')),
        (DISPENSARY, _('Dispensary')),
        (DISTRICT_HEALTH_OFFICE, _('District Health Office')),
        (DISTRICT_HOSPITAL, _('District Hospital')),
        (EYE_CENTRE, _('Eye Centre')),
        (EYE_CLINIC, _('Eye Clinic')),
        (HEALTH_CENTRE, _('Health Centre')),
        (HEALTH_PROGRAMME, _('Health Programme')),
        (HEALTH_PROJECT, _('Health Project')),
        (LABORATORY, _('Laboratory (Stand-alone)')),
        (MATERNITY_HOME, _('Maternity Home')),
        (MEDICAL_CENTRE, _('Medical Centre')),
        (MEDICAL_CLINIC, _('Medical Clinic')),
        (MEDICAL_CLINIC, _('Medical Clinic')),
        (NURSING_HOME, _('Nursing Home')),
        (OTHER, _('Other')),
        (OTHER_HOSPITAL, _('Other Hospital    ')),
        (PROVINCIAL_GENERAL_HOSPITAL, _('Provincial General Hospital')),
        (RADIOLOGY_UNIT, _('Radiology Unit')),
        (SUB_DISTRICT_HOSPITAL, _('Sub-District Hospital')),
        (TRAINING_INSTITUTION_IN_HEALTH, _('Training Institution in Health (Stand-alone)')),
        (VCT_CENTRE, _('VCT Centre (Stand-Alone)')),
    ]

    AF = 1
    LA = 2
    MISS = 3
    MOH = 4
    OTHER_MIN = 6
    PRIVATE = 7

    AGENCY_CHOICES = [
        (AF, _('AF')),
        (LA, _('LA')),
        (MISS, _('MISS')),
        (MOH, _('MOH')),
        (NGO, _('NGO')),
        (OTHER_MIN, _('OTHER MIN')),
        (PRIVATE, _('PRIVATE')),
        (NA, _('NA')),
    ]

    NOT_OPERATIONAL = 1
    OPERATIONAL = 2
    PENDING_OPENING = 3

    STATUS_CHOICES = [
        (NOT_OPERATIONAL, _('Not-Operational')),
        (OPERATIONAL, _('Operational')),
        (PENDING_OPENING, _('Pending Opening')),
        (UNKOWN, _('Unknown')),
    ]

    ACADEMIC = 1
    ARMED_FORCES = 2
    CHRISTIAN_HEALTH_ASSOCIATION_OF_KENYA = 3
    COMMUNITY = 4
    COMPANY_MEDICAL_SERVICE = 5
    DEVELOPMENT_FUND = 6
    HUMANITARIAN_AGENCIES = 7
    KENYA_EPISCOPAL_CONFERENCE_CATHOLIC_SECRETARIAT = 8
    LOCAL_AUTHORITY = 9
    MINISTRY_OF_HEALTH = 10
    OTHER_FAITH_BASED = 12
    OTHER_PUBLIC_INSTITUTION = 13
    PARASTATAL = 14
    PRIVATE_ENTERPRISE = 15
    PRIVATE_PRACTICE_CLINICAL_OFFICER = 16
    PRIVATE_PRACTICE_GENERAL_PRACTITIONER = 17
    PRIVATE_PRACTICE_MEDICAL_SPECIALIST = 18
    PRIVATE_PRACTICE_NURSE_MIDWIFE = 19
    PRIVATE_PRACTICE_UNSPECIFIED = 20
    STATE_COORPORATION = 21
    SUPKEM = 22
    T_FUND = 23

    OWNER_CHOICES = [
        (ACADEMIC, _('Academic (if registered)')),
        (ARMED_FORCES, _('Armed Forces')),
        (CHRISTIAN_HEALTH_ASSOCIATION_OF_KENYA, _('Christian Health Association of Kenya')),
        (COMMUNITY, _('Community')),
        (COMPANY_MEDICAL_SERVICE, _('Company Medical Service')),
        (DEVELOPMENT_FUND, _('Development Fund')),
        (HUMANITARIAN_AGENCIES, _('Humanitarian Agencies')),
        (KENYA_EPISCOPAL_CONFERENCE_CATHOLIC_SECRETARIAT,
         _('Kenya Episcopal Conference-Catholic Secretariat')),
        (LOCAL_AUTHORITY, _('Local Authority')),
        (MINISTRY_OF_HEALTH, _('Ministry of Health')),
        (NGO, _('Non-Governmental Organizations')),
        (OTHER_FAITH_BASED, _('Other Faith Based')),
        (OTHER_PUBLIC_INSTITUTION, _('Other Public Institution')),
        (PARASTATAL, _('Parastatal')),
        (PRIVATE_ENTERPRISE, _('Private Enterprise (Institution)')),
        (PRIVATE_PRACTICE_CLINICAL_OFFICER, _('Private Practice - Clinical Officer')),
        (PRIVATE_PRACTICE_GENERAL_PRACTITIONER, _('Private Practice - General Practitioner')),
        (PRIVATE_PRACTICE_MEDICAL_SPECIALIST, _('Private Practice - Medical Specialist')),
        (PRIVATE_PRACTICE_NURSE_MIDWIFE, _('Private Practice - Nurse / Midwife')),
        (PRIVATE_PRACTICE_UNSPECIFIED, _('Private Practice - Unspecified')),
        (STATE_COORPORATION, _('State Corporation')),
        (SUPKEM, _('Supreme Council for Kenya Muslims')),
        (T_FUND, _('T Fund')),
        (UNKOWN, _('Unknown')),
    ]

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    name = models.CharField(_("Facility Name"), max_length=255, blank=False)
    slug = AutoSlugField(verbose_name=_("Slug"), populate_from='name', unique=True)
    description = models.TextField(_("Description"), default="", blank=True)

    facility_code = models.PositiveIntegerField(
        _("Facility Code"), unique=True, blank=True, null=True, default=None)
    facility_number = models.PositiveIntegerField(
        _("Facility Number"), unique=True, blank=True, null=True, default=None)
    hmis = models.PositiveIntegerField(_("HMIS"), unique=True, blank=True, null=True, default=None)
    level = models.PositiveIntegerField(_("KEPH Level"), choices=LEVEL_CHOICES, default=UNKOWN)
    facility_class = models.PositiveIntegerField(
        _("Facility Classification"), unique=True, blank=True, null=True, default=None)
    facility_type = models.PositiveIntegerField(_("Type"), choices=TYPE_CHOICES, default=OTHER)
    owner = models.PositiveIntegerField(_("Owner"), choices=OWNER_CHOICES, default=UNKOWN)
    agency = models.PositiveIntegerField(_("Agency"), choices=AGENCY_CHOICES, default=NA)
    status = models.PositiveIntegerField(
        _("Operational Status"), choices=STATUS_CHOICES, default=OPERATIONAL)

    county = models.ForeignKey(County, verbose_name=_("County"), on_delete=models.PROTECT)
    province = models.ForeignKey(
        Province, verbose_name=_("Province"), blank=True, null=True, default=None, on_delete=models.PROTECT)
    district = models.ForeignKey(
        District, verbose_name=_("District"), blank=True, null=True, default=None, on_delete=models.PROTECT)
    division = models.ForeignKey(
        Division, verbose_name=_("Division"), blank=True, null=True, default=None, on_delete=models.PROTECT)
    location = models.ForeignKey(
        Location, verbose_name=_("Location"), blank=True, null=True, default=None, on_delete=models.PROTECT)
    sub_location = models.ForeignKey(SubLocation, verbose_name=_(
        "Sub Location"), blank=True, null=True, default=None, on_delete=models.PROTECT)
    constituency = models.ForeignKey(
        Constituency, verbose_name=_("Constituency"), blank=True, null=True, default=None, on_delete=models.PROTECT)
    plot_number = models.CharField(_("Plot Number"), max_length=255, blank=True, default="")
    location_description = models.TextField(_("Description of Location"), default="", blank=True)
    nearest_town = models.CharField(_("Nearest Town"), max_length=255, blank=True, default="")

    landline = PhoneNumberField(_('Official Land-line'), max_length=255, blank=True)
    mobile = PhoneNumberField(_('Official Mobile'), max_length=255, blank=True)
    alternate_no = PhoneNumberField(
        _('Official Alternate Phone Number'), max_length=255, blank=True)
    fax = PhoneNumberField(_('Official Fax'), max_length=255, blank=True)

    email = models.EmailField(_("Official Email"), max_length=255, blank=True)

    address = models.CharField(_("Official Address"), max_length=255, blank=True, default="")
    town = models.CharField(_("Town"), max_length=255, blank=True, default="")
    post_code = models.CharField(_("Post Code"), max_length=255, blank=True, default="")

    in_charge = models.CharField(_("In Charge"), max_length=255, blank=True, default="")
    in_charge_title = models.CharField(
        _("Job Title of in Charge"), max_length=255, blank=True, default="")

    beds = models.PositiveIntegerField(_("Beds"), unique=True, blank=True, null=True, default=None)
    cots = models.PositiveIntegerField(_("Cots"), unique=True, blank=True, null=True, default=None)

    twenty_four_hour = models.NullBooleanField(_("Open 24 Hours"), default=None)
    open_weekends = models.NullBooleanField(_("Open Weekends"), default=None)
    anc = models.NullBooleanField(_("ANC"), default=None)
    art = models.NullBooleanField(_("ART"), default=None)
    beoc = models.NullBooleanField(_("BEOC"), default=None)
    blood = models.NullBooleanField(_("BLOOD"), default=None)
    caes_sec = models.NullBooleanField(_("CAES SEC"), default=None)
    ceoc = models.NullBooleanField(_("CEOC"), default=None)
    cimci = models.NullBooleanField(_("C-IMCI"), default=None)
    epi = models.NullBooleanField(_("EPI"), default=None)
    fp = models.NullBooleanField(_("FP"), default=None)
    growm = models.NullBooleanField(_("GROWM"), default=None)
    hbc = models.NullBooleanField(_("HBC"), default=None)
    hct = models.NullBooleanField(_("HCT"), default=None)
    ipd = models.NullBooleanField(_("IPD"), default=None)
    opd = models.NullBooleanField(_("OPD"), default=None)
    outreach = models.NullBooleanField(_("Outreach"), default=None)
    pmtct = models.NullBooleanField(_("PMTCT"), default=None)
    rad_xray = models.NullBooleanField(_("RAD/XRAY"), default=None)
    rhtc_rhdc = models.NullBooleanField(_("RHTC/RHDC"), default=None)
    tb_diag = models.NullBooleanField(_("TB Diagnosis"), default=None)
    tb_labs = models.NullBooleanField(_("TB Labs"), default=None)
    tb_treat = models.NullBooleanField(_("TB Treatment"), default=None)
    youth = models.NullBooleanField(_("Youth"), default=None)

    active = models.BooleanField(_("Active"), default=True)

    latitude = models.DecimalField(
        _("Latitude"), max_digits=9, decimal_places=6, null=True, blank=True, default=None)
    longitude = models.DecimalField(
        _("Longitude"), max_digits=9, decimal_places=6, null=True, blank=True, default=None)

    # Geo Django field to store a point
    coordinates = models.PointField(_("Coordinates"), null=True, blank=True, default=None, help_text=_(
        "Represented as (longitude, latitude)"))

    # You MUST use GeoManager to make Geo Queries
    objects = GeoFacilityManager()

    def save(self, *args, **kwargs):
        if self.longitude and self.latitude:
            self.coordinates = Point(float(self.longitude), float(self.latitude))
        super(HealthFacility, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Health Facility")
        verbose_name_plural = _("Health Facilities")

    def __str__(self):
        return self.name

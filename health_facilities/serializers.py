from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from .models import FacilityOwner, FacilityType, HealthFacility
from .search_indexes import HealthFacilityIndex

from places.serializers import ProvinceSerializer, ConstituencySerializer, CountySerializer
from places.serializers import DistrictSerializer, DivisionSerializer, LocationSerializer
from places.serializers import SubLocationSerializer


class FacilityOwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = FacilityOwner

        fields = ('id', 'created_on', 'updated_on', 'name')
        read_only_fields = ('id', 'created_on', 'updated_on', 'name')


class FacilityTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FacilityType

        fields = ('id', 'created_on', 'updated_on', 'name')
        read_only_fields = ('id', 'created_on', 'updated_on', 'name')


class HealthFacilitySerializer(serializers.ModelSerializer):
    owner = FacilityOwnerSerializer(read_only=True, required=False)
    facility_type = FacilityTypeSerializer(read_only=True, required=False)
    province = ProvinceSerializer(read_only=True, required=False)
    county = CountySerializer(read_only=True, required=False)
    constituency = ConstituencySerializer(read_only=True, required=False)
    district = DistrictSerializer(read_only=True, required=False)
    division = DivisionSerializer(read_only=True, required=False)
    location = LocationSerializer(read_only=True, required=False)
    sub_location = SubLocationSerializer(read_only=True, required=False)

    class Meta:
        model = HealthFacility

        fields = (
            'id',
            'created_on',
            'updated_on',
            'slug',
            'name',
            'description',
            'facility_code',
            'facility_number',
            'hmis',
            'level',
            'facility_class',
            'facility_type',
            'owner',
            'agency',
            'status',
            'county',
            'province',
            'district',
            'division',
            'location',
            'sub_location',
            'constituency',
            'plot_number',
            'location_description',
            'nearest_town',
            'landline',
            'mobile',
            'alternate_no',
            'fax',
            'landline_unverified',
            'mobile_unverified',
            'alternate_no_unverified',
            'fax_unverified',
            'email',
            'address',
            'town',
            'post_code',
            'in_charge',
            'in_charge_title',
            'beds',
            'cots',
            'twenty_four_hour',
            'open_weekends',
            'anc',
            'art',
            'beoc',
            'blood',
            'caes_sec',
            'ceoc',
            'cimci',
            'epi',
            'fp',
            'growm',
            'hbc',
            'hct',
            'ipd',
            'opd',
            'outreach',
            'pmtct',
            'rad_xray',
            'rhtc_rhdc',
            'tb_diag',
            'tb_labs',
            'tb_treat',
            'youth',
            'active',
            'coordinates',
            # computed fields
            'get_level_display',
            'get_agency_display',
            'get_status_display',
            'get_twenty_four_hour',
            'get_open_weekends',
            'get_anc',
            'get_art',
            'get_beoc',
            'get_blood',
            'get_caes_sec',
            'get_ceoc',
            'get_cimci',
            'get_epi',
            'get_fp',
            'get_growm',
            'get_hbc',
            'get_hct',
            'get_ipd',
            'get_opd',
            'get_outreach',
            'get_pmtct',
            'get_rad_xray',
            'get_rhtc_rhdc',
            'get_tb_diag',
            'get_tb_labs',
            'get_tb_treat',
            'get_youth',
        )
        read_only_fields = (
            'id',
            'created_on',
            'updated_on',
            'slug',
            'name',
            'active',
            'facility_code',
            'province',
            'constituency',
            'district',
            'division',
            'location',
            'sub_location',
            'county',
        )


class HealthFacilitySearchSerializer(HaystackSerializer):

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [HealthFacilityIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text",
            "rendered",
            "name",
            "slug",
            "id",
            "county",
            "province",
            "district",
            "division",
            "location",
            "sub_location",
            "constituency",
            "facility_type",
            "owner",
            "level",
            "agency",
            "status",
        ]

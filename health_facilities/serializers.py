from rest_framework import serializers

from .models import FacilityOwner, FacilityType, HealthFacility


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

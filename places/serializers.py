from rest_framework import serializers

from places.models import County, Constituency, Province, District
from places.models import Division, Location, SubLocation


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province

        fields = ('id', 'created_on', 'updated_on', 'slug', 'name')
        read_only_fields = ('id', 'created_on', 'updated_on', 'slug', 'name')


class CountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County

        fields = ('id', 'created_on', 'updated_on', 'slug', 'name')
        read_only_fields = ('id', 'created_on', 'updated_on', 'slug', 'name')


class DistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District

        fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'province')
        read_only_fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'province')


class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division

        fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'district')
        read_only_fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'district')


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location

        fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'division')
        read_only_fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'division')


class SubLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubLocation

        fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'location')
        read_only_fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'location')


class ConstituencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Constituency

        fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'county')
        read_only_fields = ('id', 'created_on', 'updated_on', 'slug', 'name', 'county')

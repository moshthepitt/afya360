#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

from django.conf import settings
from django.contrib.gis.geos import Point
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

import phonenumbers

from places.models import County, Constituency, Province, District
from places.models import Division, Location, SubLocation

from .models import HealthFacility, FacilityType, FacilityOwner


def search_model_choices(data, model_choice_tuple):
    choices = [(x[0], str(x[1])) for x in model_choice_tuple]
    if data == "Not in List" and model_choice_tuple == HealthFacility.TYPE_CHOICES:
        data = "Other"
    result = [v[0] for v in choices if v[1] == data]
    try:
        return result[0]
    except IndexError:
        print (data, choices)
        raise(IndexError)


def prepare_phone(data):
    number_list = [s for s in data.split() if s.isdigit()]
    possible_bumber = "".join(number_list)
    try:
        phone = phonenumbers.parse(possible_bumber, "KE")
        if phonenumbers.is_valid_number(phone):
            return "+{}{}".format(phone.country_code, phone.national_number)
    except:
        pass
    return ""


def prepare_email(data):
    try:
        validate_email(data)
        return data
    except ValidationError:
        return ""


def prepare_null_bool(data):
    if data == "Y" or data == "y":
        return True
    elif data == "N" or data == "n":
        return False
    else:
        return None


def import_health_facilities():
    """
        Import from laest ehealth.or.ke files
        Does not deal with:
            facility_number
            hmis
            level
            facility_class
            agency
            plot_number
            description

        Run:
            from health_facilities.import_facilities import import_health_facilities
            import_health_facilities()
    """
    filename = "{}/documentation/data/ehealth.csv".format(settings.BASE_DIR)

    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        other_type, created = FacilityType.objects.get_or_create(name="Other")
        other_owner, created = FacilityOwner.objects.get_or_create(name="Unknown")
        for row in reader:
            print "{0} - {1}".format(row[0].strip(), row[1].strip())
            facility = HealthFacility()

            facility.facility_code = int(row[0].strip())
            facility.name = row[1].strip()

            if row[2]:
                province, created = Province.objects.get_or_create(name=row[2].strip().upper())
            if row[3]:
                county, created = County.objects.get_or_create(name=row[3].strip().upper())
            if row[4]:
                district = District.objects.filter(name=row[4].strip().upper()).first()
                if not district:
                    district, created = District.objects.get_or_create(name=row[4].strip().upper(), province=province)
            if row[5]:
                division, created = Division.objects.get_or_create(name=row[5].strip().upper(), district=district)
            if row[11]:
                constituency = Constituency.objects.filter(name=row[11].strip().upper()).first()
                if not constituency:
                    constituency, created = Constituency.objects.get_or_create(name=row[11].strip().upper(), county=county)
            if row[8]:
                location, created = Location.objects.get_or_create(name=row[8].strip().upper(), division=division)
            if row[9]:
                sub_location, created = SubLocation.objects.get_or_create(name=row[9].strip().upper(), location=location)

            facility.province = province
            facility.county = county
            facility.district = district
            facility.division = division
            facility.location = location
            facility.sub_location = sub_location
            facility.constituency = constituency

            if row[6]:
                facility.facility_type, created = FacilityType.objects.get_or_create(name=row[6].strip())
            else:
                facility.facility_type = other_type

            if row[7]:
                facility.owner, created = FacilityOwner.objects.get_or_create(name=row[7].strip())
            else:
                facility.owner = other_owner

            if row[10]:
                facility.location_description = row[10].strip()
            if row[12]:
                facility.nearest_town = row[12].strip()

            if row[13]:
                facility.beds = int(row[13].strip())
            if row[14]:
                facility.cots = int(row[14].strip())

            if row[15]:
                facility.landline = prepare_phone(row[15].strip())
                facility.landline_unverified = row[15].strip()
            if row[16]:
                facility.fax = prepare_phone(row[16].strip())
                facility.fax_unverified = row[16].strip()
            if row[17]:
                facility.mobile = prepare_phone(row[17].strip())
                facility.mobile_unverified = row[17].strip()
            if row[20]:
                facility.alternate_no = prepare_phone(row[20].strip())
                facility.alternate_no_unverified = row[20].strip()

            if row[18]:
                facility.email = prepare_email(row[18].strip())
            if row[19]:
                facility.address = row[19].strip()

            if row[21]:
                facility.town = row[21].strip()
            if row[22]:
                facility.post_code = row[22].strip()
            if row[23]:
                facility.in_charge = row[23].strip()
            if row[24]:
                facility.in_charge_title = row[24].strip()

            facility.twenty_four_hour = prepare_null_bool(row[25].strip())
            facility.open_weekends = prepare_null_bool(row[26].strip())

            if row[27]:
                facility.status = search_model_choices(row[27].strip(), HealthFacility.STATUS_CHOICES)

            facility.anc = prepare_null_bool(row[28].strip())
            facility.art = prepare_null_bool(row[29].strip())
            facility.beoc = prepare_null_bool(row[30].strip())
            facility.blood = prepare_null_bool(row[31].strip())
            facility.caes_sec = prepare_null_bool(row[32].strip())
            facility.ceoc = prepare_null_bool(row[33].strip())
            facility.cimci = prepare_null_bool(row[34].strip())
            facility.epi = prepare_null_bool(row[35].strip())
            facility.fp = prepare_null_bool(row[36].strip())
            facility.growm = prepare_null_bool(row[37].strip())
            facility.hbc = prepare_null_bool(row[38].strip())
            facility.hct = prepare_null_bool(row[39].strip())
            facility.ipd = prepare_null_bool(row[40].strip())
            facility.opd = prepare_null_bool(row[41].strip())
            facility.outreach = prepare_null_bool(row[42].strip())
            facility.pmtct = prepare_null_bool(row[43].strip())
            facility.rad_xray = prepare_null_bool(row[44].strip())
            facility.rhtc_rhdc = prepare_null_bool(row[45].strip())
            facility.tb_diag = prepare_null_bool(row[46].strip())
            facility.tb_labs = prepare_null_bool(row[47].strip())
            facility.tb_treat = prepare_null_bool(row[48].strip())
            facility.youth = prepare_null_bool(row[49].strip())

            facility.save()

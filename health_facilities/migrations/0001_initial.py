# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import django.contrib.gis.db.models.fields
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacilityOwner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Facility Owner',
                'verbose_name_plural': 'Facility Owners',
            },
        ),
        migrations.CreateModel(
            name='FacilityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Facility Type',
                'verbose_name_plural': 'Facility Types',
            },
        ),
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255, verbose_name='Facility Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=b'name', unique=True, verbose_name='Slug')),
                ('description', models.TextField(default=b'', verbose_name='Description', blank=True)),
                ('facility_code', models.PositiveIntegerField(default=None, unique=True, null=True, verbose_name='Facility Code', blank=True)),
                ('facility_number', models.PositiveIntegerField(default=None, unique=True, null=True, verbose_name='Facility Number', blank=True)),
                ('hmis', models.PositiveIntegerField(default=None, unique=True, null=True, verbose_name='HMIS', blank=True)),
                ('level', models.PositiveIntegerField(default=999, verbose_name='KEPH Level', choices=[(1, 'Level 1'), (2, 'Level 2'), (3, 'Level 3'), (4, 'Level 4'), (5, 'Level 5'), (6, 'Level 6'), (999, 'Not Classified')])),
                ('facility_class', models.PositiveIntegerField(default=None, unique=True, null=True, verbose_name='Facility Classification', blank=True)),
                ('agency', models.PositiveIntegerField(default=998, verbose_name='Agency', choices=[(1, 'AF'), (2, 'LA'), (3, 'MISS'), (4, 'MOH'), (996, 'NGO'), (6, 'OTHER MIN'), (7, 'PRIVATE'), (998, 'NA')])),
                ('status', models.PositiveIntegerField(default=2, verbose_name='Operational Status', choices=[(1, 'Not-Operational'), (2, 'Operational'), (3, 'Pending Opening'), (999, 'Unknown')])),
                ('plot_number', models.CharField(default=b'', max_length=255, verbose_name='Plot Number', blank=True)),
                ('location_description', models.TextField(default=b'', verbose_name='Description of Location', blank=True)),
                ('nearest_town', models.CharField(default=b'', max_length=255, verbose_name='Nearest Town', blank=True)),
                ('landline', phonenumber_field.modelfields.PhoneNumberField(max_length=255, verbose_name='Official Land-line', blank=True)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=255, verbose_name='Official Mobile', blank=True)),
                ('alternate_no', phonenumber_field.modelfields.PhoneNumberField(max_length=255, verbose_name='Official Alternate Phone Number', blank=True)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(max_length=255, verbose_name='Official Fax', blank=True)),
                ('landline_unverified', models.CharField(default=b'', max_length=50, verbose_name='Official Land-line', blank=True)),
                ('mobile_unverified', models.CharField(default=b'', max_length=50, verbose_name='Official Mobile Unverified', blank=True)),
                ('alternate_no_unverified', models.CharField(default=b'', max_length=50, verbose_name='Official Alternate Phone Number Unverified', blank=True)),
                ('fax_unverified', models.CharField(default=b'', max_length=50, verbose_name='Official Fax Unverified', blank=True)),
                ('email', models.EmailField(max_length=255, verbose_name='Official Email', blank=True)),
                ('address', models.CharField(default=b'', max_length=255, verbose_name='Official Address', blank=True)),
                ('town', models.CharField(default=b'', max_length=255, verbose_name='Town', blank=True)),
                ('post_code', models.CharField(default=b'', max_length=255, verbose_name='Post Code', blank=True)),
                ('in_charge', models.CharField(default=b'', max_length=255, verbose_name='In Charge', blank=True)),
                ('in_charge_title', models.CharField(default=b'', max_length=255, verbose_name='Job Title of in Charge', blank=True)),
                ('beds', models.PositiveIntegerField(default=None, unique=True, null=True, verbose_name='Beds', blank=True)),
                ('cots', models.PositiveIntegerField(default=None, unique=True, null=True, verbose_name='Cots', blank=True)),
                ('twenty_four_hour', models.NullBooleanField(default=None, verbose_name='Open 24 Hours')),
                ('open_weekends', models.NullBooleanField(default=None, verbose_name='Open Weekends')),
                ('anc', models.NullBooleanField(default=None, help_text='Antenatal Care', verbose_name='ANC')),
                ('art', models.NullBooleanField(default=None, help_text='Anti-retroviral Therapy', verbose_name='ART')),
                ('beoc', models.NullBooleanField(default=None, help_text='Basic Essential Obstetric Care', verbose_name='BEOC')),
                ('blood', models.NullBooleanField(default=None, help_text='Blood Transfusion', verbose_name='BLOOD')),
                ('caes_sec', models.NullBooleanField(default=None, help_text='', verbose_name='CAES SEC')),
                ('ceoc', models.NullBooleanField(default=None, help_text='', verbose_name='CEOC')),
                ('cimci', models.NullBooleanField(default=None, help_text='Community Integrated Management of Childhood Illness', verbose_name='C-IMCI')),
                ('epi', models.NullBooleanField(default=None, help_text='Expanded Program on Immunization', verbose_name='EPI')),
                ('fp', models.NullBooleanField(default=None, help_text='Family Planning', verbose_name='FP')),
                ('growm', models.NullBooleanField(default=None, help_text='', verbose_name='GROWM')),
                ('hbc', models.NullBooleanField(default=None, help_text='Home Based Care', verbose_name='HBC')),
                ('hct', models.NullBooleanField(default=None, help_text='', verbose_name='HCT')),
                ('ipd', models.NullBooleanField(default=None, help_text='Inpatient Department', verbose_name='IPD')),
                ('opd', models.NullBooleanField(default=None, help_text='Outpatient Department', verbose_name='OPD')),
                ('outreach', models.NullBooleanField(default=None, help_text='', verbose_name='Outreach')),
                ('pmtct', models.NullBooleanField(default=None, help_text='Prevention of Mother-to-child Transmission of HIV', verbose_name='PMTCT')),
                ('rad_xray', models.NullBooleanField(default=None, help_text='Radiography / X-Ray', verbose_name='RAD/XRAY')),
                ('rhtc_rhdc', models.NullBooleanField(default=None, help_text='', verbose_name='RHTC/RHDC')),
                ('tb_diag', models.NullBooleanField(default=None, help_text='', verbose_name='TB Diagnosis')),
                ('tb_labs', models.NullBooleanField(default=None, help_text='', verbose_name='TB Labs')),
                ('tb_treat', models.NullBooleanField(default=None, help_text='', verbose_name='TB Treatment')),
                ('youth', models.NullBooleanField(default=None, help_text='Youth Friendly Service', verbose_name='Youth')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('latitude', models.DecimalField(decimal_places=6, default=None, max_digits=9, blank=True, null=True, verbose_name='Latitude')),
                ('longitude', models.DecimalField(decimal_places=6, default=None, max_digits=9, blank=True, null=True, verbose_name='Longitude')),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(default=None, srid=4326, blank=True, help_text='Represented as (longitude, latitude)', null=True, verbose_name='Coordinates')),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='places.Constituency', null=True, verbose_name='Constituency')),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='County', to='places.County')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='places.District', null=True, verbose_name='District')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='places.Division', null=True, verbose_name='Division')),
                ('facility_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Type', to='health_facilities.FacilityType')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='places.Location', null=True, verbose_name='Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Owner', to='health_facilities.FacilityOwner')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='places.Province', null=True, verbose_name='Province')),
                ('sub_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='places.SubLocation', null=True, verbose_name='Sub Location')),
            ],
            options={
                'verbose_name': 'Health Facility',
                'verbose_name_plural': 'Health Facilities',
            },
        ),
    ]

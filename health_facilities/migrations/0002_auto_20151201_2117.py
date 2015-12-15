# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_facilities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facilityowner',
            options={'ordering': ['name'], 'verbose_name': 'Facility Owner', 'verbose_name_plural': 'Facility Owners'},
        ),
        migrations.AlterModelOptions(
            name='facilitytype',
            options={'ordering': ['name'], 'verbose_name': 'Facility Type', 'verbose_name_plural': 'Facility Types'},
        ),
        migrations.AlterModelOptions(
            name='healthfacility',
            options={'ordering': ['name'], 'verbose_name': 'Health Facility', 'verbose_name_plural': 'Health Facilities'},
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='caes_sec',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='CAES SEC'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='ceoc',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='CEOC'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='growm',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='GROWM'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='hct',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='HCT'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='landline_unverified',
            field=models.CharField(default=b'', max_length=50, verbose_name='Official Land-line Unverified', blank=True),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='outreach',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='Outreach'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='rhtc_rhdc',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='RHTC/RHDC'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='tb_diag',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='TB Diagnosis'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='tb_labs',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='TB Labs'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='tb_treat',
            field=models.NullBooleanField(default=None, help_text='', verbose_name='TB Treatment'),
        ),
    ]

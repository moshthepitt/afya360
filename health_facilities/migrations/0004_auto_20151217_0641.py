# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_facilities', '0003_auto_20151216_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthfacility',
            name='caes_sec',
            field=models.NullBooleanField(default=None, help_text='Caesaraen Section', verbose_name='CAES SEC'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='ceoc',
            field=models.NullBooleanField(default=None, help_text='Comprehensive Emergency Obstetric Care', verbose_name='CEOC'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='growm',
            field=models.NullBooleanField(default=None, help_text='Growth Monitoring and Promotion', verbose_name='GROWM'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='hct',
            field=models.NullBooleanField(default=None, help_text='HIV Counselling and Testing', verbose_name='HCT'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='outreach',
            field=models.NullBooleanField(default=None, help_text='Outreach services in the Community', verbose_name='Outreach'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='rad_xray',
            field=models.NullBooleanField(default=None, help_text='Radioology Services (e.g. X-ray, MRI, Ultrascan etc)', verbose_name='RAD/XRAY'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='rhtc_rhdc',
            field=models.NullBooleanField(default=None, help_text='Rural Health Training or Demonstration Centre', verbose_name='RHTC/RHDC'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='tb_diag',
            field=models.NullBooleanField(default=None, help_text='Tuberculosis Diagnosis', verbose_name='TB Diagnosis'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='tb_labs',
            field=models.NullBooleanField(default=None, help_text='Tuberculosis Labs', verbose_name='TB Labs'),
        ),
        migrations.AlterField(
            model_name='healthfacility',
            name='tb_treat',
            field=models.NullBooleanField(default=None, help_text='Tuberculosis Treatment', verbose_name='TB Treatment'),
        ),
    ]

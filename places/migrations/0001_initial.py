# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(
                    auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(
                    populate_from=b'name', unique_with=(b'county__name',),
                    editable=False)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Constituency',
                'verbose_name_plural': 'Constituencies',
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(
                    auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(
                    populate_from=b'name', unique_with=(b'county__name',),
                    editable=False)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'County',
                'verbose_name_plural': 'Counties',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(
                    auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(
                    populate_from=b'name', unique_with=(b'province__name',),
                    editable=False)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'District',
                'verbose_name_plural': 'Districts',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(
                    auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(
                    populate_from=b'name', unique_with=(b'district__name',),
                    editable=False)),
                ('district', models.ForeignKey(verbose_name='District',
                                               to='places.District',
                                               on_delete=models.PROTECT)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Division',
                'verbose_name_plural': 'Divisions',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(
                    auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(
                    populate_from=b'name', unique_with=(b'division__name',),
                    editable=False)),
                ('division', models.ForeignKey(verbose_name='Division',
                                               to='places.Division',
                                               on_delete=models.PROTECT)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(
                    auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(
                    populate_from=b'name', unique_with=(b'county__name',),
                    editable=False)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
        ),
        migrations.CreateModel(
            name='SubLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False,
                                        auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(
                    auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(
                    auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255,
                                          verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(
                    populate_from=b'name', unique_with=(b'location__name',),
                    editable=False)),
                ('location', models.ForeignKey(verbose_name='Location',
                                               to='places.Location',
                                               on_delete=models.PROTECT)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Sub Location',
                'verbose_name_plural': 'Sub Locations',
            },
        ),
        migrations.AddField(
            model_name='district',
            name='province',
            field=models.ForeignKey(verbose_name='Province',
                                    to='places.Province',
                                    on_delete=models.PROTECT),
        ),
        migrations.AddField(
            model_name='constituency',
            name='county',
            field=models.ForeignKey(verbose_name='County',
                                    to='places.County',
                                    on_delete=models.PROTECT),
        ),
    ]

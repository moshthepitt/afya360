#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
import csv
from time import sleep

from django.conf import settings
from django.contrib.gis.geos import Point


def get_urls():
    """
      The URL struction seems to be a common base URL with a GET paramenter
      that is the healthfacility code
      like so: http://www.ehealth.or.ke/facilities/facility.aspx?fas=11509
      Since we know some codes, we can general the urls
    """
    filename = "{}/documentation/data/ehealth.csv".format(settings.BASE_DIR)

    with open(filename, "rb") as ifile:
        reader = csv.reader(ifile)
        data = zip(reader)
    base = "http://www.ehealth.or.ke/facilities/facility.aspx?fas="
    return {x: "{0}{1}".format(base, x) for x in [x[0][0] for x in data]}


def crawl():
    """
    A function to assist in crawling http://www.ehealth.or.ke/ to find the coordinates of health facilities

    Basically based on:
        r = requests.get("http://www.ehealth.or.ke/facilities/facility.aspx?fas=11509")
        string = r.text
        p = re.compile(r"GLatLng\(([0-9\.\-]+).*?([\.\-0-9]+)\)")
        p.findall(string)
        [('-3.38928', '38.56007'), ('-3.38928', '38.56007')]
    """
    result = {}
    urls = get_urls()
    if urls:
        n = 0
        for code, url in urls.iteritems():
            n += 1
            sleep(0.3)
            r = requests.get(url)
            string = r.text
            p = re.compile(r"GLatLng\(([0-9\.\-]+).*?([\.\-0-9]+)\)")
            possible = p.findall(string)
            if possible:
                coordinate = possible[0]
                point = Point(float(coordinate[1]), float(coordinate[0]))
                result[code] = point
            if n == 10:
                break
    filename = "{}/documentation/data/coordinates.csv".format(settings.BASE_DIR)
    with open(filename, 'wb') as myfile:
        writer = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for k, v in result.iteritems():
            writer.writerow([k, (v.x, v.y)])

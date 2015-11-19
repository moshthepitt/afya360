"""
A file to assist in crawling http://www.ehealth.or.ke/ to find the coordinates of health facilities

Basically based on:
    r = requests.get("http://www.ehealth.or.ke/facilities/facility.aspx?fas=11509")
    string = r.text
    p = re.compile(r"GLatLng\(([0-9\.\-]+).*?([\.\-0-9]+)\)")
    p.findall(string)
    [('-3.38928', '38.56007'), ('-3.38928', '38.56007')]
"""

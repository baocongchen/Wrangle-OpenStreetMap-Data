"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

OSMFILE = "irvine"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", 
            "Trail", "Parkway", "Commons"]


mapping = { "St": "Street",
            "St.": "Street",
            "Ave": "Avenue",
            "Rd.": "Road",
            "Rd":  "Road",
            "Blvd": "Boulevard",
            "Blvd.": "Boulevard",
            "Bl": "Boulevard",
            "DRIVE": "Drive",
            "Dr": "Drive",
            "Ct": "Court",
            "Ct.": "Court",
            "Pl": "Place",
            "Sq": "Square",
            "La": "Lane",
            "Ln": "Lane",
            "Tr": "Trail",
            "Pkwy": "Parkway",
            "Pkwy.": "Parkway",
            "Cmns": "Commons"
            }


def audit_street_type(street_types, street_name):
    """audits street type"""
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    """returns True if element is street name"""
    return (elem.attrib['k'] == "addr:street" or elem.attrib['k'] == "exit_to")


def audit(osmfile):
    """audits osmfile for street and key type info, and returns street types"""
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    osm_file.close()
    return street_types



 




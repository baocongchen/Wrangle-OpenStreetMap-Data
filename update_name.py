import re
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

def update_name(name, mapping):
    """update street name to value in mapping"""
    for key in mapping:
        if re.search("[^a-z]"+key+"[^a-z]", name):
            if "." in key:
                name = name.replace(key, mapping[key])
            else:
                if key + "." in name:
                    name = name.replace(key + ".", mapping[key])
                else:
                    name = name.replace(key, mapping[key])
            break
    return name   
import re
d5 = re.compile(r'^\d{5}$')
d5_d4 = re.compile(r'^(\d{5})-\d{4}$')
w2_d5 = re.compile(r'^[a-zA-Z]{2}\s(\d{5})$')
d5_c  = re.compile(r'^(\d{5}).+$')

def audit_postcode(postcode):
	"""detects pattern and returns clean postcode"""
	if re.match(d5, postcode):
	    return postcode
	elif re.match(d5_d4, postcode):
	    clean_postcode = re.findall(d5_d4, postcode)[0]
	elif re.match(w2_d5, postcode):                                                 
		clean_postcode = re.findall(w2_d5, postcode)[0]
	elif re.match(d5_c, postcode):
		clean_postcode = re.findall(d5_c, postcode)[0]
	return clean_postcode

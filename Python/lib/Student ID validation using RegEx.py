import re  


if re.search(r'^[0-9][0-9][0-9][0-9]-[\d]+-[\d]+$', input()):
	print("Valid")
else:
	print("Invalid")

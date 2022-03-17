# get the "issuedAtUtc" for the most recently issued credential and get the credential id associated with it
# This may need changing if product grows
def get_credId():
	import requests
	
	url = "https://api.trinsic.id/credentials/v1/credentials"

	headers = {
	    "Accept": "application/json",
	    "Authorization": "Bearer VDKTn73klPr3xDPXNuRjAopk1GB7oFziOTU-t2QVscU"
	}
	
	response = requests.request("GET", url, headers=headers)
	api_data = response.json()
	utc_list = []
	# apend to a list and compare with the most recent one to see which is greater
	
	# get the utc times into a list
	for d in api_data:
	    for key, value in d.items():
	        if key == "issuedAtUtc":
	            utc_list.append(d.get("issuedAtUtc"))
	            maximum = max(utc_list)
	# get the verification url associated with the most recent time
	for d in api_data:
	    for key, value in d.items():
	        if value == maximum:
	            cred_id = d["credentialId"]
	return cred_id
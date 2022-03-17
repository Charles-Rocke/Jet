from app.Constants.contants import SCHEMA_NAME
def get_def():
	import requests
	url = "https://api.trinsic.id/credentials/v1/definitions/credentials"

	headers = {
		"Accept": "application/json",
		"Authorization": "NdIdxyi5HonBbW5UjbtXbt-CKiWPQk5cTzlL_aOcFnQ"
	}

	list_def = []
	response = requests.request("GET", url, headers=headers)
	listData = response.json()
	for data in listData:
		for key, value in data.items():
			if value == SCHEMA_NAME:
				def_id = data["definitionId"]
				list_def.append(def_id)
				break
	# get id out of list and return it
	for id in list_def:
		final_id = id
		return final_id
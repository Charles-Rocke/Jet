def open_wallet():
	import json
	json_profile ={}
	
	# open wallet for email and first name
	with open("Profile.json", "r") as profile_data:
	  user_data = json.load(profile_data)
	wallet_id = user_data['walletId']
	
	email = user_data['email']
	fname = user_data['first name']

	# push data into field for signup
	json_profile['email'] = email
	json_profile['first name'] = fname
	return json_profile
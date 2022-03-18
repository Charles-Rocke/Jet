# Create a cloud wallet in the form of a file
# Create new wallet for user 
# Accept user name and walletId as arguments
# This function creates a cloud wallet,
# writes the wallet id to the cloud wallet,
# and is capable of receiveing credentials
def cloud_wallet(fname, lname, email, wallet_id):
	
	# New algorithm
	"""Create a file that stores data in .json format
		 Data to store:
			Users Full name
			email
			walletId
			Jet generated password
	"""
	import json
	json_profile ={}

	#accept arguments
	user_email = email
	user_fname = fname
	user_lname = lname
	user_walletId = wallet_id

	#prepare data for .json dump
	json_profile['first name'] = user_fname
	json_profile['last name'] = user_lname
	json_profile['email'] = user_email
	json_profile['walletId'] = user_walletId

	# creating a wallet in json format
	# write the above data to a json file
	with open("Profile.json", "w") as user_profile:
	  json.dump(json_profile, user_profile)

	# file name = cloud_wallet or cw
	cw_name = user_name
	# walletId will be put in a list
	wallet = [walletId]
	
	# Open the file for writing
	# This creates a new filename.
	with open(cw_name, "w") as cw:
		for walletId in wallet:
			cw.write(walletId)
	
	print(f"Done writing to file {cw}")

# Sign-up for a new site
# need to store email and  Jet generated password in json
# open the wallet and get the data to input into the browser
def jet_signup():
	import json
	json_profile ={}
	#Browser action
	
	# read the newly created file
	with open("Profile.json", "r") as profile_data:
	  user_data = json.load(profile_data)

		# extract user data for sign-up
	email = user_data['email']
	fname = user_data['first name']
	lname = user_data['last name']
	wallet_id = user_data['walletId']

	# push data into field for signup
	json_profile['first name'] = fname
	json_profile['last name'] = lname
	json_profile['email'] = email
	json_profile['walletId'] = wallet_id
	return 
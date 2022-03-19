# Use the cloud wallet to automatically present and login
# this method gets a cloud wallet id and autmoatically presents a credential for verification/login
# combines retieving walletId
# generating a verification url,
# and presenting credentials
def signin():
	import requests
	import json
	from app.Constants.constants import API_KEY
	from trinsic.service_clients import CredentialsClient, WalletClient, ServiceClientCredentials
	from app.Constants import constants


	# Credentials API
	credentials_client = CredentialsClient(ServiceClientCredentials(API_KEY))
	credentials_client.config.retry_policy.retries = 0
	
	# Wallet API
	wallet_client = WalletClient(ServiceClientCredentials(API_KEY))
	wallet_client.config.retry_policy.retries = 0

	# generate verification url
	policy_id = constants.policy_id
	verification = credentials_client.create_verification_from_policy(policy_id)
	  # Get the most recent verification
	url = "https://api.trinsic.id/credentials/v1/verifications"
	headers = {
	  "Accept": "text/plain",
	  "Authorization": "Bearer NdIdxyi5HonBbW5UjbtXbt-CKiWPQk5cTzlL_aOcFnQ"
  }

	response = requests.request("GET", url, headers=headers)
	json_resp = response.json()
	utc_list = []
	# apend to a list and compare with the most recent one to see which is greater
	# get the utc times into a list
	for d in json_resp:
		for key, value in d.items():
			if key == "updatedAtUtc":
				utc_list.append(d.get("updatedAtUtc"))
				maximum = max(utc_list)
	# get the verification url associated with the most recent time
	for d in json_resp:
		for key, value in d.items():
			if value == maximum:
				verif_url = d["verificationRequestUrl"]
				verif_id = d['verificationId']
	# 2.
	with open("Profile.json", "r") as profile_data:
	  user_data = json.load(profile_data)
	wallet_id = user_data['walletId']
	# 3.
	wallet_client.submit_verification_from_data_auto_select(wallet_id, verif_url)




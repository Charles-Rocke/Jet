# Get wallet
import requests

def get_w():

	# List wallets API
	url = "https://api.trinsic.id/wallet/v1/api/wallets"
	headers = {"Accept": "text/plain"}
	response = requests.request("GET", url, headers=headers)

	# Get correct wallet
	
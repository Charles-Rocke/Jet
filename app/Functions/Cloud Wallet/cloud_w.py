import requests

# 'Click login button'
# open 'cloud wallet' (file)
# get the walletId
# present the walletId for verification/login

# First we need to get then store the walletId in a file

# Create new wallet for user 
# Accept user name and walletId as arguments
def cloud_wallet(user_name, walletId):

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
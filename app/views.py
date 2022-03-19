from app.SDK.sdk import wallet_client
from app.Functions.Auth import signup, signin
from app.Functions.Get import issuedAt, def_id
from flask import Blueprint, render_template, request, redirect, url_for
import uuid
from app.Constants.constants import API_KEY
from trinsic.service_clients import CredentialsClient, WalletClient, ServiceClientCredentials


# Credentials API
credentials_client = CredentialsClient(ServiceClientCredentials(API_KEY))
credentials_client.config.retry_policy.retries = 0

# Wallet API
wallet_client = WalletClient(ServiceClientCredentials(API_KEY))
wallet_client.config.retry_policy.retries = 0

views = Blueprint('views', __name__)


# Home view 
@views.route('/', methods=['GET', 'POST'])
def home():
		if request.method == 'POST':
			# get user name
			user_fname = request.form.get('fname')
			user_lname = request.form.get('lname')
			user_email = request.form.get('user_email')
			# create cloud wallet
			owner_name = user_fname + " " + user_lname  # Can be None
			wallet_id = None  # Can be None
			# if 'Bad Request' here:
				# delete some of the cloud wallets created
			wallet = wallet_client.create_wallet({
			  "ownerName": owner_name,
			  "wallet_id": wallet_id
			})
			print("wallet created")
			# create cloud wallet
			signup.cloud_wallet(user_fname, user_lname, user_email, wallet.wallet_id)
			print("cloud wallet created")
			
			# auto issue credential
			connection_id = None  # Can be null | <connection identifier>
			automatic_issuance = True
			print("creating credential")
			credential_values = {
			  "First Name": user_fname,
			  "Email": user_email,
				"Account ID" : uuid.uuid4()
			}
			credential = credentials_client.create_credential({
			  "definitionId": "CP8tWh3qwcD4rSy3fcfRrT:3:CL:284024:tag",
			  "connectionId": connection_id,
			  "automaticIssuance": automatic_issuance,
			  "credentialValues": credential_values
			})
			print("got def id and credential offered")
			# auto accept credential
			cred_url = issuedAt.get_credurl()
			wallet_id = wallet.wallet_id
			print("got cred_id and wallet_id")
			credential = wallet_client.accept_credential(wallet_id, cred_url)
			print("redirecting to login")
			return redirect(url_for('views.login'))
		return render_template("home.html")

# Create cloud wallet view
@views.route('/welcome', methods=['GET', 'POST'])
def welcome():
	
	return render_template("welcome.html")

@views.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		# open the cloud wallet file
		# retrieve the walletId
		signin.signin()
		return redirect(url_for('views.welcome'))
	return render_template("login.html")


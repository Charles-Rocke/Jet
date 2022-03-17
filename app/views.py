from app.SDK.sdk import wallet_client
from app.Functions.Auth import signup, login
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
			user_name = request.form.get('user_name')
			user_email = request.form.get('user_email')
			# create cloud wallet
			owner_name = None  # Can be None
			wallet_id = None  # Can be None
			wallet = wallet_client.create_wallet({
			  "ownerName": user_name,
			  "wallet_id": wallet_id
			})
			# create cloud wallet in app
			signup.cloud_wallet(user_name, wallet.wallet_id)

			# auto issue credential
			connection_id = None  # Can be null | <connection identifier>
			automatic_issuance = True
			credential_values = {
			  "First Name": user_name,
			  "Email": user_email,
				"Account ID" : uuid.uuid4()
			}
			credential = credentials_client.create_credential({
			  "definitionId": def_id.get_def(),
			  "connectionId": connection_id,
			  "automaticIssuance": automatic_issuance,
			  "credentialValues": credential_values
			})

			# auto accept credential
			credential = wallet_client.accept_credential_offer(wallet.wallet_id, issuedAt.get_credId())
			
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
		login.login()
		return redirect(url_for('views.welcome'))
	return render_template("login.html")


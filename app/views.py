from app.SDK.sdk import wallet_client
from app.Functions.Auth import signup
from flask import Blueprint, render_template, request, redirect, url_for
import uuid

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
			signup.cloud_wallet(user_name, wallet.walletId)

			# auto issue credential
			connection_id = None  # Can be null | <connection identifier>
			automatic_issuance = True
			credential_values = {
			  "First Name": user_name,
			  "Email": user_email,
				"Account ID" : uuid.uuid4()
			}
			credential = credentials_client.create_credential({
			  "definitionId": definition_id,
			  "connectionId": connection_id,
			  "automaticIssuance": automatic_issuance,
			  "credentialValues": credential_values
			})

			# auto accept credential
			### Get credential id and wallet id
			credential = wallet_client.accept_credential_offer(wallet.wallet_id, credential_id)
			return redirect(url_for('views.create_wallet'))
		return render_template("home.html")

# Create cloud wallet view
@views.route('/create-wallet', methods=['GET', 'POST'])
def create_wallet():
	
	return render_template("create-wallet.html")

@views.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		
	return render_template("login.html")
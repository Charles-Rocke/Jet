from app.SDK.sdk import wallet_client
from app.Functions.Auth import signup, signin, auth_func
from app.Functions.Get import issuedAt, def_id
from flask import Blueprint, render_template, request, redirect, url_for, flash
import uuid
from app.Constants.constants import API_KEY
from trinsic.service_clients import CredentialsClient, WalletClient, ServiceClientCredentials
from flask_login import login_required, current_user, login_user
from .models import Note, User
from . import db

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
			# p4msp4m is Full name & haven is First Name
			credential_values = {
			  "Full Name": user_fname,
			  "Email": user_email,
				"Account ID" : uuid.uuid4()
			}
			# change the way the definition id is recieved
			credential = credentials_client.create_credential({
			  "definitionId": "A2Ands9NsWKPXkrDR8ELic:3:CL:283274:tag",
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
			print(cred_url)
			
			# retrieve wallet
			json_profile = auth_func.open_wallet()
			# retrieve email and first name from cloud wallet
			email = json_profile['email']
			firstName = json_profile['first name']
	
			user = User.query.filter_by(email=email).first()
			if user:
					flash('Email already exists', category='error')
			elif len(email) < 4:
					flash('Email must be longer than 3 characters.', category = 'error')
			elif len(firstName) < 2:
					flash('Firstname must be longer than 1 character.', category = 'error')
			else:
					# add user to the data base
					new_user = User(email=email, fname=firstName)
					db.session.add(new_user)
					db.session.commit()
					login_user(new_user, remember=True)
					flash('Account created!', category = 'success')
					return redirect(url_for('views.welcome'))
			return redirect(url_for('auth.login'))
		return render_template("home.html")

# Create cloud wallet view
@views.route('/welcome', methods=['GET', 'POST'])
def welcome():
	
	return render_template("welcome.html", user=current_user)
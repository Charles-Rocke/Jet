from app.SDK.sdk import wallet_client
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


# Home view 
@views.route('/', methods=['GET', 'POST'])
def home():
		if request.method == 'POST':
			# get user name
			user_name = request.form.get('user_name')

			# create cloud wallet
			owner_name = None  # Can be None
			wallet_id = None  # Can be None
			wallet = wallet_client.create_wallet({
			  "ownerName": user_name,
			  "wallet_id": wallet_id
			})
			return redirect(url_for('views.create_wallet'))
		return render_template("home.html")

# Create cloud wallet view
@views.route('/create-wallet', methods=['GET', 'POST'])
def create_wallet():
	
	return render_template("create-wallet.html")
from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


# Home view 
@views.route('/', methods=['GET', 'POST'])
def home():
		
	return render_template("home.html", user=current_user)

# Create cloud wallet view
@views.route('/create-wallet', methods=['GET', 'POST'])
def create_wallet():
		if request.method == 'POST':
			# get user name
			user_name = #form input

			# create cloud wallet
			owner_name = None  # Can be None
			wallet_id = None  # Can be None
			wallet = wallet_client.create_wallet({
			  "ownerName": owner_name,
			  "wallet_id": wallet_id
			})
			return redirect(url_for('views.home'))
	return render_template("create-wallet.html", user=current_user)
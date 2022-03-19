from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from app.Functions.Auth import signup, signin, auth_func


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
	
	if request.method == 'POST':
		json_profile = auth_func.open_wallet()
		# retrieve email from cloud wallet
		email = json_profile['email']
		fname = json_profile['first name']

		user = User.query.filter_by(email=email).first()
		if user:
			# run verification
			signin.signin()
			# log user in
			login_user(user, remember=True)
			return redirect(url_for('views.welcome'))
		else:
				flash('Account does not exist', category='error')
	return render_template('login.html', user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
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
				new_user = User(email=email, firstName=firstName)
				db.session.add(new_user)
				db.session.commit()
				login_user(new_user, remember=True)
				flash('Account created!', category = 'success')
				return redirect(url_for('views.welcome'))

	return render_template('new_sign_up.html', user=current_user)
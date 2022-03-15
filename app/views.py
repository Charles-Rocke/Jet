from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


# Home view 
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
		
	return render_template("home.html", user=current_user)
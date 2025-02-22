from flask import render_template
from app.users import users_bp

@users_bp.route('/profile')
def profile():
    return render_template('users/profile.html')

from flask import render_template
from app.settings import settings_bp


@settings_bp.route('/')
def settings():
    return render_template('settings/settings.html')
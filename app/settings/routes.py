from flask import render_template, jsonify
from app.settings import settings_bp
from app import db


@settings_bp.route('/')
def settings():
    return render_template('settings/settings.html')


@settings_bp.route('/create_db')
def create_db():
    db.create_all()
    return jsonify('Updated succefull!!!')
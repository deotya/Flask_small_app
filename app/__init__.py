from flask import Flask
from app.extensions import db
from app.main import main_bp
from app.users import users_bp
from app.settings import settings_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)  # Inițializare baza de date

    # Înregistrare Blueprint-uri
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(settings_bp)

    return app

from flask import Flask
from app.extensions import db, migrate
from app.main import main_bp
from app.users import users_bp
from app.settings import settings_bp



def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)  # Inițializare baza de date
    migrate.init_app(app, db)

    # Înregistrare Blueprint-uri
    app.register_blueprint(main_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(settings_bp)

    from app import models


    return app
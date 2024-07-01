import os
from flask import Flask
from .routes.note import note_bp
from .routes.login import login_bp
from .routes.errors import errors_bp
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'database-new.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'secret-key'
    app.register_blueprint(note_bp) 
    app.register_blueprint(login_bp) 
    app.register_blueprint(errors_bp)

    from .model import db
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    return app



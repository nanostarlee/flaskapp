from flask_login import LoginManager
import os
from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy

# db variable initialization
db = SQLAlchemy()

TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def create_app():
    app = Flask(__name__, template_folder=TEMPLATES_FOLDER)
    app = Flask(__name__, static_folder=STATIC_FOLDER)
    app.config.from_object(app_config['development'])
    db.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')

    from .models import User, Note

    # create_database(app)
    login_manager = LoginManager()
    login_manager.login_view ='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
# def create_database(app):
#         db.create_all(app=app)
#         print('Database created successfully!')

    

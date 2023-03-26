from flask import Flask
from os import path

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'THE CYBER SAVVY NINJAS'

    # after defining blueprints, we need to register them here
    from .views import views

    app.register_blueprint(views, url_prefix='/')    # specifies a prefix that we have to put before any of the blueprint paths

    return app

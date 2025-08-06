from flask import Flask
from .main import main_dp

def creation():
    app = Flask(__name__)
    app.register_blueprint(main_dp)
    return app



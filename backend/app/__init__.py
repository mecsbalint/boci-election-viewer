from flask import Flask
from app.database.sqlalchemy import init_flask_sqlalchemy


def create_app():

    app = Flask(__name__)

    init_flask_sqlalchemy(app)

    return app

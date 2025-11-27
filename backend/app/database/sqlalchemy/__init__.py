from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DATABASE_URI

sql_alchemy = SQLAlchemy()


def init_flask_sqlalchemy(app: Flask):

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    sql_alchemy.init_app(app)

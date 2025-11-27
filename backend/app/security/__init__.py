from flask import Flask
from app.config import JWT_SECRET_KEY
from app.security.flask_jwt_extended_config import init_flask_jwt


def init_security(app: Flask):
    init_flask_jwt(app, JWT_SECRET_KEY)

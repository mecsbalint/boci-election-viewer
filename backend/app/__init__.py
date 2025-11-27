from flask import Flask
from app.controllers import init_endpoints
from app.database import init_db
from app.security import init_security


def create_app():

    app = Flask(__name__)

    init_db(app)

    init_endpoints(app)

    init_security(app)

    return app

from flask import Flask
from .user_controllers import init_user_endpoints


def init_endpoints(app: Flask):
    init_user_endpoints(app)

from typing import Any
from flask import Flask
from flask_jwt_extended import JWTManager


def init_flask_jwt(app: Flask, jwt_secret_key: str):

    jwt = JWTManager()

    app.config["JWT_SECRET_KEY"] = jwt_secret_key
    jwt.init_app(app)

    @jwt.user_lookup_loader  # pyright: ignore[reportUnknownMemberType]
    def user_lookup_callback(jwt_header: dict[str, Any], jwt_payload: dict[str, Any]) -> int:  # pyright: ignore[reportUnusedFunction]
        user_id = int(jwt_payload["sub"])
        return user_id

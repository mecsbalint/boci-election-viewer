from typing import cast
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URI = os.getenv("DATABASE_URI")
PORT = int(cast(str, os.getenv("PORT")))
JWT_SECRET_KEY = cast(str, os.getenv("JWT_SECRET_KEY"))

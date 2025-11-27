from app.database.sqlalchemy import sql_alchemy


class User(sql_alchemy.Model):
    __tablename__ = "users"

    id = sql_alchemy.Column('student_id', sql_alchemy.Integer, primary_key=True)
    name = sql_alchemy.Column(sql_alchemy.String(100))
    email = sql_alchemy.Column(sql_alchemy.String(100), unique=True)
    password = sql_alchemy.Column(sql_alchemy.String())

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password

from app.database.sqlalchemy import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String())

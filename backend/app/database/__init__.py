from flask import Flask
from app.database.sqlalchemy import init_flask_sqlalchemy
import psycopg2
import os
from app.config import DATABASE_URI


def init_db(app: Flask):
    run_sql_script("drop_tables.sql")
    run_sql_script("initialization.sql")

    init_flask_sqlalchemy(app)


def run_sql_script(file_name: str):
    sql_file_path = os.path.join(os.path.dirname(__file__), file_name)
    with open(sql_file_path) as sql_file:
        sql = sql_file.read()

    connection = psycopg2.connect(DATABASE_URI)
    connection.autocommit = True
    cursor = connection.cursor()

    for statement in sql.split(";"):
        stmt = statement.strip()
        if stmt:
            cursor.execute(stmt + ";")

    cursor.close()
    connection.close()

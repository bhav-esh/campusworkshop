"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr1o8rddl9mmohhpc0-a.oregon-postgres.render.com",
        database="todo_nfif",
        user="root",
        password="uHOYF52cuybzBbMRwuOvuLwNPN4HNbhl")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes

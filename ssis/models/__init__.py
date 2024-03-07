import mysql.connector as mysql
from os import getenv

db = mysql.connect(
            host = getenv('host'),
            user = getenv('username'),
            password = getenv('password'),
            database = getenv('dbname')
        )
cursor = db.cursor()
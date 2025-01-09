import mysql.connector
from dotenv import load_dotenv
import os
import time

load_dotenv()

db_config={
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

def db_conn():
    return mysql.connector.connect(**db_config)


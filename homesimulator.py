import mysql.connector
from dotenv import load_dotenv
import os
import datetime
import random
import time
load_dotenv()

db_config={
    'host': "localhost",
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}

kitchen_query="INSERT INTO kitchen(date, value) VALUES (%s, %s)"
bedroom_query= "INSERT INTO bedroom(date, value) VALUES (%s, %s)"
livingroom_query= "INSERT INTO livingroom(date, value) VALUES (%s, %s)"
bathroom_query= "INSERT INTO bathroom(date, value) VALUES (%s, %s)"

queries = [
    kitchen_query,
    bedroom_query,
    livingroom_query,
    bathroom_query
]

def db_conn():
    return mysql.connector.connect(**db_config)

def simulator():
    connection=db_conn()
    cursor=connection.cursor()

    time_stamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    for query in queries:
        rand_val=random.randint(100,1000)
        data=(time_stamp,rand_val)
        cursor.execute(query,data)
        print(query,data)

    connection.commit()
    cursor.close()
    connection.close()
    
while True:
    simulator()
    print("Data sent")
    time.sleep(10)
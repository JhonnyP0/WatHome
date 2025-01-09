from flask import Flask, request,render_template
import mysql.connector
from dotenv import load_dotenv
import os

app = Flask(__name__)

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

@app.route("/")
def example_page():
    return render_template("examplePage.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
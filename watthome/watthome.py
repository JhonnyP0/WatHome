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
def base():
    return render_template("base.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/dailyusage")
def dailyusage():
    return render_template("dailyusage.html")

@app.route("/actualusage")
def actualusage():
    return render_template("actualusage.html")

@app.route("/monthlyusage")
def monthlyusage():
    return render_template("monthlyusage.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
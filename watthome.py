from flask import Flask, request,render_template,Response,url_for
import mysql.connector
from dotenv import load_dotenv
import os
import plotly
import plotly.graph_objects as go
import json



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
    months = ["00:00","01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00"]
    kitchen = [9, 3, 1, 10, 4, 10, 7, 5, 8, 6, 3, 9, 12, 6, 7, 3, 5, 8, 2, 4, 10, 11, 6, 8]
    bedroom = [7, 5, 10, 8, 9, 3, 12, 2, 11, 4, 6, 7, 9, 5, 10, 6, 4, 8, 3, 7, 11, 12, 6, 9]
    livingroom = [8, 6, 4, 9, 7, 5, 12, 3, 11, 9, 2, 6, 7, 8, 10, 11, 5, 9, 6, 7, 12, 4, 8, 6]
    bathroom = [10, 7, 3, 6, 5, 12, 4, 8, 11, 9, 10, 7, 6, 4, 12, 3, 5, 9, 8, 7, 10, 6, 11, 5]

    # Tworzenie wykresu liniowego
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=months,
        y=kitchen,
        mode='lines+markers',  # Linia + punkty
        name='kitchen',
        line=dict(color='rgba(226, 226, 15, 0.934)')
    ))

    fig.add_trace(go.Scatter(
        x=months,
        y=bedroom,
        mode='lines+markers',  # Linia + punkty
        name='bedroom',  # Nazwa dla tej linii
        line=dict(color='green', width=4)
    ))
    fig.add_trace(go.Scatter(
        x=months,
        y=livingroom,
        mode='lines+markers',  # Linia + punkty
        name='livingroom',  # Nazwa dla tej linii
        line=dict(color='blue', width=4)
    ))
    fig.add_trace(go.Scatter(
        x=months,
        y=bathroom,
        mode='lines+markers',  # Linia + punkty
        name='bathroom',  # Nazwa dla tej linii
        line=dict(color='red', width=4)
    ))

    # Ustawienia wykresu
    fig.update_layout(
    title='Daily Usage Over Months',
    xaxis_title='Time',
    yaxis_title='Power Consumpted [W]',
    template='plotly_dark',
    plot_bgcolor='rgba(0,0,0,0)',  # Przezroczyste tło wykresu
    paper_bgcolor='rgba(0,0,0,0)',  # Przezroczyste tło całego wykresu
    xaxis=dict(
        title_font=dict(color='yellow'),
        showgrid=False,
        zeroline=True,
        gridcolor='gray'
    ),
    yaxis=dict(
        title_font=dict(color='yellow'),
        showgrid=False,
        zeroline=True,
        gridcolor='gray'
    ),
    autosize=True,  # Automatyczne dopasowanie rozmiaru  # Ustawienie szerokości wykresu
    height=400,     # Ustawienie wysokości wykresu

    dragmode=False
    )

    # Konwertowanie wykresu na format JSON
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    # Renderowanie strony i przekazanie danych wykresu
    return render_template('dailyusage.html', graph_json=graph_json)

@app.route("/actualusage")
def actualusage():
    return render_template("actualusage.html")

@app.route("/monthlyusage")
def monthlyusage():
    return render_template("monthlyusage.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
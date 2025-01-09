FROM python:3.9-slim

# Instalacja zależności systemowych
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie pliku requirements.txt i instalacja zależności Pythona
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie całej aplikacji do obrazu
COPY . /app/

# Eksponowanie portu
EXPOSE 5050

# Domyślny punkt wejścia
CMD ["python", "watthome.py"]

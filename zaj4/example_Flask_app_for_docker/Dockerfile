FROM python:3.12-alpine

# Ustawienie katalogu roboczego
WORKDIR /app

# Kopiowanie plików do kontenera
COPY . .

# Instalacja zależności
RUN pip install -r requirements.txt


# Definiowanie domyślnego polecenia uruchomienia
CMD ["python", "app.py"]

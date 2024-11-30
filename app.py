from flask import Flask
from dotenv import load_dotenv
import os

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# Tworzymy aplikację Flask
app = Flask(__name__)

# Konfigurujemy aplikację przy pomocy zmiennych środowiskowych
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URI'] = os.getenv('DATABASE_URI')

@app.route('/')
def home():
    return 'Welcome to the app!'

if __name__ == '__main__':
    app.run(debug=True)


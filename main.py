import os

from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    send_from_directory,
)

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Set secret key from .env file
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename, cache_timeout=60*60*24*365)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/frankies')
def frankies():
    return render_template('frankies.html')

@app.route('/studio')
def studio():
    return render_template('studio.html')

@app.route('/water-purification')
def water_purification():
    return render_template('water_purification.html')

if __name__ == "__main__":
    app.run()

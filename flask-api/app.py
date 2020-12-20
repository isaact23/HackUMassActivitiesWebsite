#!/usr/bin/env python3

# Import Flask modules to communicate with React frontend
from flask import Flask
from flask_cors import CORS
# Import Python files to scrape the internet on the backend
from src.scrape import scrape

app = Flask(__name__)
CORS(app)


# Get data from /src/scrape/scrape.py. Called by App.js.
# filters is a string of 0s and 1s representing which filters are enabled.
@app.route('/scrape/<filters>')
def scrape_data(filters=None):
    return scrape.get_activity_data(filters)

from flask import Flask
from flask import render_template

from json2table import convert
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html', data=convert(get_data(), build_direction="LEFT_TO_RIGHT", table_attributes={"border":1}))

def get_data():
    key = os.environ['CIVIC_INFORMATION_API_KEY']
    return requests.get("https://www.googleapis.com/civicinfo/v2/representatives?address=11218&key="+key).json()

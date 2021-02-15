from flask import Flask
from datetime import date

app = Flask(__name__)
from app import views

DATE = 'February,14,2021'
from flask import Flask, render_template,url_for,request
from database import get_data

app = Flask(__name__)


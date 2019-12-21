# -*- coding: utf-8 -*-

from flask import render_template, request
from app import app
from model import get_prediction

@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html")

@app.route('/input')
def flight_input():
    return render_template("input.html")

@app.route('/output')
def flight_output():
    origin = request.args.get('Origin')
    dest = request.args.get('Destination')
    airline = request.args.get('Airline')
    date = request.args.get('Date')
    hour = request.args.get('Hour')

    prediction = get_prediction(origin, dest, airline, date, hour)

    return render_template("output.html", result=prediction)
from flask import Flask, render_template, request, jsonify, redirect
import sqlite3
import random
import cv2
import numpy as np
import pandas as pd
import csv
import serial

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('web/index.html')


@app.route('/rooms')
def rooms():
    return render_template('web/rooms.html')


@app.route('/about')
def about():
    return render_template('web/about.html')


@app.route('/submit')
def submit():
    random_code = request.form['random_code']
    check_in = request.form['CheckIn']
    check_out = request.form['CheckOut']
    adults = request.form['adults']
    children = request.form['children']

    # Write form data to CSV file
    with open('booking_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([check_in, check_out, adults, children])


if __name__ == '__main__':
    app.run(debug=True)

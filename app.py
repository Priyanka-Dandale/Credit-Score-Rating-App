# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 15:13:18 2022

@author: p.santosh.dandale
"""
#importing required libraries
from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = b'priyanka178'

#app routing to url
@app.route("/priyankad")
def index():
    flash("What's your credit score?")
    return render_template("index.html")

#app routing after submitting user input
@app.route("/submit", methods=["POST","GET"])
def output():
    flash("Hi, you entered your credit score = " + str(request.form['num_input'])+".")
    if int(request.form['num_input']) < 200:
        flash("Your score is Poor!!! ")
    elif (int(request.form['num_input']) >= 200 and int(request.form['num_input']) < 450):
        flash("Your score is Average!!! ")
    elif (int(request.form['num_input']) >= 450 and int(request.form['num_input']) < 650):
        flash("Your score is Good!!! ")
    else:
        flash("Your score is Excellent!!! ")
    return render_template("index.html")




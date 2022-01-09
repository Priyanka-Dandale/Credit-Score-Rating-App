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
    if (int(request.form['num_input']) >= 300 and int(request.form['num_input']) < 350):
        flash("Your score is Poor!!! ")
    elif (int(request.form['num_input']) >= 350 and int(request.form['num_input']) < 600):
        flash("Your score is Average!!! ")
    elif (int(request.form['num_input']) >= 600 and int(request.form['num_input']) < 800):
        flash("Your score is Good!!! ")
    elif (int(request.form['num_input']) >= 800 and int(request.form['num_input']) < 901):
        flash("Your score is Excellent!!! ")
    else:
        flash("Your score is Invalid. Maximum limit is 900 and Minimum limit is 300. ")
    return render_template("index.html")





# views.py

from flask import Flask, redirect, url_for, request, render_template

from app import app


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        feelings = request.form
        print(feelings)
        return redirect(url_for('about', feelings=feelings))
    else:
        return render_template("index.html")


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


@app.route('/result')
def result():
    return render_template("result.html")

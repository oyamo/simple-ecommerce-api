from . import app
from  flask import jsonify, render_template
from os import path

@app.route('/',  methods=['GET', 'POST'])
def index():
    return render_template("endpoints.html")

@app.route('/favicon.ico')
def favicon():
    return jsonify(data = 'null')
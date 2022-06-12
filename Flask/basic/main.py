from flask import *
import datetime

app = Flask('app')

@app.route('/')
def index():
    return "<h1>Hello World</h1>"

app.run(host="localhost", port=8080, debug=True)

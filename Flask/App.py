from flask import *
import requests
import flask
import json

app = Flask(__name__)


@app.route('/ip')
def index():
    string = str(request.full_path)
    try:
        lst = string.strip().split()
    except Exception:
        lst = [0, 0]
    return str(string) + str(lst[1])


def run():
    app.run()


if __name__ == '__main__':
    run()

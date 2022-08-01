from flask import *
from flask_cors import CORS
import json

app = Flask('app')
with open("config.json") as file:
    app.config = json.load(file)

CORS(app)

@app.route('/favicon.ico/')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/welcome/')
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)

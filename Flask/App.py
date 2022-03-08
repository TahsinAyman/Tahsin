from flask import Flask, render_template
import flask

app = Flask(__name__)
lst = (1, 2, 3)


@app.route('/')
def index():
    return render_template('data.json')


@app.route('/home')
def home():
    return lst


if __name__ == '__main__':
    app.run(debug=True)

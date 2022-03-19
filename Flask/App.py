from flask import Flask, render_template
import flask

app = Flask(__name__)
lst = [{"name": "Tahsin"}]


@app.route('/')
def index():
    return render_template('data.json')


@app.route('/home')
def home():
    return str(lst)


def run():
    app.run()
    
if __name__ == '__main__':
    run()

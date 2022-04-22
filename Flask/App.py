from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

def run():
    app.run(debug=True, host='localhost', port=6969)

if __name__ == '__main__':
    run()

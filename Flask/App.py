from flask import *

app = Flask('app')
app.secret_key = 'asaasas'


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>Hello World..</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

from flask import Flask


app = Flask('app')

@app.route("/")
def home():
   return "<h1>Hello</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
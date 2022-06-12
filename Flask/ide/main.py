from flask import *
from subprocess import getoutput

app = Flask(__name__)
app.config['SECRET_KEY'] = "556767789900000bb000bb211212121"

@app.route('/', methods=['GET'])
def index():
    return render_template("ide.html")

@app.route("/run/", methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        code = request.form['code']
        with open('file.py', 'w') as file:
            file.write(code)
        # string = ''
        string = getoutput("file.py")
        return str(string)
    else:
        return "Error!"



def main():
    app.run(debug=True, host="localhost", port=8080)

if __name__ == '__main__':
    main()

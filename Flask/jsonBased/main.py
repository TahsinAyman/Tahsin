from flask import *
import json

app = Flask('app')

@app.route("/", methods=['GET'])
def index():
    style = ""
    with open('settings.json') as file:
        data = json.load(file)
    try:
        if data['theme'] == "Dark":
            style = """body {
    margin: 0;
    font-family: "Courier New";
    background-color: black;
}
h1 {
    color: white;
}
h2 {
    color: white;
}
h3 {
    color: white;
}
h4 {
    color: white;
}
h5 {
    color: white;
}
h6 {
    color: white;
}
p {
    color: white;
}
li {
    color: white;
}
a {
    color: white;
}
p {
    color: white;
}
label {
    color: white
}
a {
    text-decoration: none;
    color: black;
}"""
        elif theme == None:
            style = ""
    except Exception:
        pass
    return render_template("home.html", css=style)

@app.route("/theme/", methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        theme = request.form['theme']
        if theme == "Dark":
            with open("settings.json") as file:
                data = json.load(file)
            data['theme'] = theme
            with open("settings.json", 'w') as file:
                json.dump(obj=data, fp=file, indent=4)
        elif theme == "Default":
            with open("settings.json") as file:
                data = json.load(file)
            data['theme'] = None
            with open("settings.json", 'w') as file:
                json.dump(obj=data, fp=file, indent=4)
        return redirect('/')
    else:
        return render_template("settings.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=80)

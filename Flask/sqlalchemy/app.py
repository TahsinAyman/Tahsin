from flask import *
from models import *


@app.route('/', methods=['GET'])
def index():
    return "Using Flask SQLALchemy"


@app.route('/person/', methods=['POST'])
def add_person():
    try:
        data = request.get_json(force=True)
        person = Person(id=data['id'], name=data['name'], age=data['age'])
        db.session.add(person)
        db.session.commit()
        data = person
        return str(data)
    except Exception as e:
        print(e)
        return jsonify({"result": False})


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)

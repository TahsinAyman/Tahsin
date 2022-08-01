from flask import *
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return json.dumps(obj={"id": self.id, "name": self.name, "age": self.age}, indent=4)


if __name__ == '__main__':
    db.create_all()

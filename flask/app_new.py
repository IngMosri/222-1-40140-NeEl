from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/neel_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
marshmallow = Marshmallow(app)

class Student(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), unique=True)
    career = database.Column(database.String(50))

    def __init__(self, name, career):
        self.name = name
        self.career = career

database.create_all()

class StudentSchema(marshmallow.Schema):
    class Meta:
        fields = ('id', 'name', 'career')

students_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@app.route('/')
def index():
    return "You are running NEEL_API"

@app.route('/create_student/', methods=['POST'])
def create_student():
    return "Estudent created"

if __name__ == "__main__":
    app.run(debug=True)
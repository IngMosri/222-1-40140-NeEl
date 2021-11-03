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
    name = request.json['name']
    #print(name)
    career = request.json['career']
    #print(career)
    new_student = Student(name,career)
    print(new_student)
    
    database.session.add(new_student)
    database.session.commit()
    
    #return "student created 102621"
    return students_schema.jsonify(new_student)

@app.route('/student/', methods=['GET'])
def get_students():
    all_students = Student.query.all()
    result = students_schema.dump(all_students)
    return jsonify(result)

@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    student = Student.query(id)
    #return id
    return students_schema.jsonify(student)

@app.route('/students_update/<id>/', methods=['PUT'])
def student_update(id):
    update = Student.query.get(id)
    name = request.json['name']
    career = request.json['career']
    
    update.name = name
    update.career = career
    database.session.commit()
    return students_schema.jsonify(update)

@app.route('/student_delete/<id>/', methods = ['DELETE'])
def student_delete(id):
    delete = Student.query.get(id)
    database.session.delete(delete)
    database.session.commit()
    return students_schema.jsonify(delete)
    





if __name__ == "__main__":
    app.run(debug=True)

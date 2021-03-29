from flask import Flask, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/openwatering.db'
db = SQLAlchemy(app)
CORS(app)

class watering_schedule(db.Model):
    date_from = db.Column(db.String(20))
    date_to = db.Column(db.String(20))
    zone_id = db.Column(db.Integer) 
    watering_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(20))
    repeat = db.Column(db.Integer)

class zones(db.Model):
    zone_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    active = db.Column(db.String(20))
    relay_port = db.Column(db.Integer)


@app.route('/funciona')
def home():
    return "funciona Ok"

@app.route('/schedule/new', methods=['POST'])
def create():
    task = watering_schedule(content = request.form['content'], status="pending")
    db.session.add(task)
    db.session.commit()
    return "saved"

@app.route('/schedule/list', methods=['GET'])
def get():
    tasks = watering_schedule.query.all()
    print(tasks)
    return jsonify(str(tasks))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= "5000")
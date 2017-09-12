# downloaded from slack
from models import Base, User, Task
from flask import Flask, jsonify, request, url_for, abort, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask.http_auth import HTTPBasicAuth

auth = HTTPBasicAuth() 

engine = create_engine('sqlite:///bagelShop.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

# ADD @auth.verify_password method here

# ADD a /users route here (POST)

# ADD a /users/id route here (GET)

@app.route('/tasks', methods = ['GET','POST'])
#protect this route with a required login
def showAllTasks():
    if request.method == 'GET':
        tasks = session.query(Task).all()
        return jsonify(tasks = [task.serialize for task in tasks])
    elif request.method == 'POST':
        name = request.json.get('name')
        description = request.json.get('description')
        duration = request.json.get('duration')
        newTask = Task(name = name, description = description, duration = duration)
        session.add(newTask)
        session.commit()
        return jsonify(newTask.serialize)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
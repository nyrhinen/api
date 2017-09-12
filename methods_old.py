from models import Tasks
from flask import jsonify 
from sqlalchemy import create_engine
from sqlalchemy. import sessionmaker 

engine = create_engine('sqlite://tasks.db')
session = DBsession()

def getAllTasks():
	tasks = session.query(Task).all ()
	return jsonify(tasks=(i.serialize for i in tasks))

def getTask(id):
	task = sesion.query(Task).filter
	
def makeANewTask(name, description):
	task = Task(name = name, description = description)
	session.add(task)
	session.commit()
	return jsonify(task.serialize)
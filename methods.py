# compile ok
from flask import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from models import Base, Task

engine = create_engine('sqlite:///tasks.db')
Base.metadata.bind = engine

DBsession = sessionmaker(bind=engine)
session = DBsession()

def getAllTasks():
	tasks = session.query(Task).all()
	print ("tasks in methods", tasks)
	return jsonify(Tasks=[i.serialize for i in tasks])
	
def getTask(id):
	task = session.query(Task).filter_by(id=id).one()
	return jsonify(Task=task.serialize)
	
def makeANewTask(name, description):
	task = Task(name = name, description = description)
	print ("task in methods", task)
	session.add(task)
	session.commit()
	return jsonify(Task=task.serialize)
		
def updateTask(id,name, description):
	task = session.query(Task).filter_by(id=id).one()
	if not name:
		task.name = name
	if not description:
		task.description = description
	session.add(task)
	session.commit()		
	return "Updating a Task with id %s" % id
	
def deleteTask(id):
	task = session.query(Task).filter_by(id=id).one()
	session.add(task)
	session.commit()		
	return "Removing task with id %s" % id
	
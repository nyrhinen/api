# imported Flask class
from flask import Flask, request
from methods import getAllTasks, getTask, makeANewTask, updateTask, deleteTask
# create instance of class
app = Flask(__name__)

@app.route("/")
@app.route("/tasks/", methods= ['GET', 'POST'])
def tasksFunction():
	if request.method == 'GET':
		# call method to get all task
		print ("call get")
		return getAllTasks()
	
	elif request.method == 'POST':
		# call method to make a new task
		print ("Making a new task")
		name = request.args.get('name', '')
		description = request.args.get('description', '')
		return makeANewTask(name, description)


@app.route("/tasks/<int:id>", methods = ['GET','PUT', 'DELETE'])
def tasksFunctionId(id):
	if request.method == 'GET':
		# call method to get specific tasks based on id
		print ("call GET id")
		return getTask(id)
	elif request.method == 'PUT':
		# call method to update a task
		name = request.args.get('name', '')
		description = request.args.get('description', '')
		return updateTask(id,name, description)
	elif request.method == 'DELETE':
		# call method to REMOVE a task
		return deleteTask(id)
		

if __name__ == ('__main__'):
	print ("main")
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
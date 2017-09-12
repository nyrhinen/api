from flask import Flask
# from methods import ...?

app = Flask(__name__)

#app.route for GET & POST
def tasksFunction():
	if request.method == 'GET':
	# call method to get all task
		print ("call get")
	elif request.method == 'POST':
	# call method to make a new task
		print ("elif")


#app.route
def tasksFunctionId(id):
	if request.method == 'GET':
	# call method to get specific tasks based on id
		print ("call GET id")
	elif request.method == 'PUT':
	# call method to update a task
		print ("PUT")
	elif request.method == 'DELETE':
	# call method to REMOVE a task
		print ("elif")
		

if __name__ == ('__main__'):
	print ("main")
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
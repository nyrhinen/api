from flask import Flask
app = Flask(__name__)

#app.route ...
def tasksFunction():
	return "Tasks listed"
	
#app.route ...
def tasksFunctionId():
	return "This method will act on the task with id %s" % id

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
from flask import Flask, request

app = Flask(__name__)

@app.route('/tasks, methods = ['GET','POST'] )
def tasksFunction():
	if (request.method == 'GET'):
		return "taks with GET"
	elif requets.method == 'POST':
		name = request.args.get('name', ''))
		desc = request.args.get('description'))
		return makeANewwTask()
		
	return "tasks function entered"

@app.route('/tasks/<int::id>, methods = ['GET','PUT', 'DELETE'])
def taskFunction(id):
	if request.method == 'GET'

if __name__ == '__main__':
	app.debug = True
	app.run(host='0,0,0,', port=5000)
from flask import Flask, jsonify
app = Flask(__name__)

# jsonify example 


userlist = [
	{
		'username': u'admin',
		'email':u'admin@localhost',
		'id':42,
		'done':False
	},
	{
		'username': u'xadmin',
		'email':u'xadmin@localhost',
		'id':4,
		'done':False
	}
]

@app.route('/_get_current_user')
def get_current_user():
	return jsonify({'user info': userlist})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
				
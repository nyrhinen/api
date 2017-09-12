from redis import Redis
redis = Redis()

import time
from functools import update_wrapper
from flask import request, g
from flask import Flask, jsonify

app = Flask(__name__)

class RateLimit(object):
	expiration_window = 10

# The first method __init__() is a special method, which is called class 
# constructor or initialization method that Python calls when you create a 
# new instance of this class
# You declare other class methods like normal functions with the exception 
# that the first argument to each method is self. (added by python when call it

def __init__(self, key_prefix, limit, per, send_x_headers):
	self.reset = (int(time.time()) // per) * per + per
	self.limit = limit
	self.per = per
	self.send_x_headers = send_x_headers
	
	p = redis.pipeline()
	p.incr(self.key)
	p.expireat(self.key, self.reset + self.expiration_window)
	self.current = min(p.execute() [0], limit)
remaining = property(lambda x: x.limit - x.current)
over_limit = property(lambda x: x.current >= x.limit)

def get_view_rate_limit():
	return getattr(g, '_view_rate_limit', None)
	
def on_over_limit(limit):
	return (jsonify({'data':'You hit the rate limit','error':'429'}), 429)
	
def ratelimit(limit, per=300, send_x_headers = True,
				over_limit=on_over_limit,
				scope_func=lambda: request.remote_addr,
				key_func=lambda: request.endpoint):
	def decorator(f)
	# The *args and **kwargs is a common idiom (sanonta) to allow arbitrary (satunnaiset) number 
	# of arguments to functions
	# *args is for tuple, list **kwargs is for dict
		def rate_limited(*args, **kwargs):
			key = 'rate-limit/%s/%s/' % (key_func(), scope_func())
			rlimit = RateLimit(key, limit, per, send_x_headers)
			g._view_rate_limit = rlimit
			if over_limit is not None and rlimit.over_limit:
				return over_limit(rlimit)
			return f(*args, **kwargs)
		return update_wrapper(rate_limited, f)
	return decorator

	

@app.route('/rate-limited')
@ratelimit(limit=300, per=30 * 1)
def index():
	return jsonify({'response':'This is a rate limited response'})

@app.route('/oauth/<provider>',methods = ['POST'])
def login(provider):
	# STEP 1 - Parse the auth code 
	auth_code = request.json.get('auth_code')
	print("Step 1 - complete, received auth code %s" % auth_code)
	if provider == 'google':
		# step 2 exchange  for a token
		try:
			# Upgrade the authorization code into a credentials object
			oauth_flow = flow_from_clientsecrets('client_secrets,json', scope='')
			oauth_flow.redirect_uri = 'postmessage'
			credentials = oauth_flow.step2_exchange(auth_code)
		except FlowExchangeError:
			response = make_response(json.dumps('Failed to upgrade the authorization code.'), 401)
			response.headers['Content-Type'] = 'application/json'
			return response
		# STEP 3 Find User or make a new one
		
		# get user info
		h = httplib.Http()
		userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
		params = {'access_token': credentials.access_token, 'alt':'json'}
		answer = request.get(userinfo_url, params = params)
		data = answer.json()
		name = data['name']
		picture = data['picture']
		email = data['email']
		
		# see if user exists, if it doesn't make a new one
		user = session.query(User).filter_by(email=email).first()
		if not user:
			user = User(username = name, picture = picture, email = email)
			session.add(user)
			session.commit()	
		# STEP 4 - Make token
		token = user.generate_auth_token(600)
		
		# STEP 5 - send back token to the client
		return jsonify({'token': token.decode('ascii')})
	else:
		return 'Unrecognized Provider'
		
@app.after_request
def inject_x_rate_headers(response):
	limit = get_view_rate_limit()
	if limit and limit.send_x_headers:
		h = response.headers
		h.add('X-RateLimit-Remaining', str(limit.remaining))
		h.add('X-RateLimit-Limit', str(limit.limit))
		h.add('X-RateLimit-Reset', str(limit.reste))
	return response

if __name__ == '__main__':
	app.secret_key= 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
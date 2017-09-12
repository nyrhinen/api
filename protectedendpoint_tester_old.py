from urllib import urlencode
from httplib2 import Http
import json
import sys
import base64

# This is old, not completed python file, urllib is problem also here.

print("running endpoint tester ... \n")
address = input("enter the address to access, \n Default: 'http://localhost:5000':    ")
if address ==  '':
	address = 'http://localhost:5000'
	
# test 1 make a new user

try: 
	url = address + '/users'
	h = Http()
	data = dict(username = "AapoKoski", password = "5alasana!")
	data = json.dumps(data)
	resp, content = h.request(url, 'POST', body = data, headers = {"Content-Type" : "application/json"})
	
	if resp['status'] != '200':
		raise Exception('received an unsuccessful status code of %s' %resp['status'])

except Exception as err:
	print("Test 2 FAILED: Could not add new task")
	print(err.args)
	sys.exit()
else:
		print("test 2 PASS:successfully created a new task")
		
#test 2 new task to the database
try: 
	h = Http()
	a.add_credentials('AapoKoski','5alasana!')
	url = address + '/tasks'
	
	data = dict(username = "AapoKoski", password = "5alasana!", name = "Homma", description = "Raskas")
	resp, content = h.request(url,'POST', body = json.dumps(data), headers = {"Content-Type" : "application/json"})
	
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print("Test 2 FAILED: Could not add new task")
	print(err.args)
	sys.exit()
else:
		print("test 2 PASS:successfully created a new task")
from urllib import urlencode
from httplib2 import Http
import json
import sys
import base64

print("Running endpoint Tester....\n")
address = input("Enter the address to access, \n Default: 'http://localhost:5000':   ")
if address == '':
	address = 'http://localhost:5000'


 #TEST 1 TRY TO MAKE A NEW USER
try:
	url = address + '/users'
 	h = Http()
 	data = dict(username = "Aapo", password = "Salasana")
 	data = json.dumps(data)
 	resp, content = h.request(url,'POST', body = data, headers = {"Content-Type": "application/json"})
	if resp['status'] != '201' and resp['status'] != '200':
 		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print("Test 1 FAILED: Could not make a new user")
	print(err.args)
	sys.exit()
else:
	print "Test 1 PASS: Succesfully made a new user"

#TEST 2 ADD NEW TASK TO THE DATABASE (WITH CREDENTIALS)
try:
	h = Http() 
	h.add_credentials('Aapo','Salasana')
	url = address + '/tasks'
	data = dict(username = "Aapo", password = "Salasana", name = "Fist task", description = "Do this as the first one", duration= "2 hours")
	resp, content = h.request(url,'POST', body = json.dumps(data), headers = {"Content-Type" : "application/json"})
	if resp['status'] != '200':
		raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
	print "Test 2 FAILED: Could not add a new task"
	print err.args
	sys.exit()
else:
	print "Test 2 PASS: Succesfully made a new task"


#TEST 3 TRY TO READ TASKS WITH INVALID CREDENTIALS
try:
	h = Http()
	h.add_credentials('Aapo','5alasana')
	url = address + '/tasks'
	resp, content = h.request(url,'GET')
	if resp['status'] == '200':
		raise Exception("Security Flaw: able to log in with invalid credentials")
except Exception as err:
	print("Test 3 FAILED")
	print(err.args)
	sys.exit()
else:
	print("Test 3 PASS: Invalid credentials - not authorized")


#TEST 4 TRY TO READ TASKS WITH VALID CREDENTIALS
try:
	h = Http()
	h.add_credentials("Aapo", "Salasana")
	url = address + '/tasks'
	resp, content = h.request(url,'GET')
	if resp['status'] != '200':
		raise Exception("Unable to access /tasks with valid credentials")
except Exception as err:
	print("Test 4 FAILED")
	print(err.args)
	sys.exit()
else:
	print("Test 4 PASS: Logged in User can view /tasks")
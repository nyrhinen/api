import httplib2
import json
import sys

print("Running Endpoint Tester....\n ")
address = input("Enter the address of the server you want to access, \n If left blank the connection will be set to 'http://localhost:5000': ")
if address == '':
   address = 'http://localhost:5000'

#Making a POST Request
print ("Making a POST Request for /tasks...")
try:
   url = address + "/tasks"
   h = httplib2.Http()
   resp, result = h.request(url, 'POST')
   if resp['status'] != '200':
      	raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
   print("Test 1 FAILED: Could not make GET Request to web server")
   print(err.args)
   sys.exit()
else:
   print("Test 1 PASS: Succesfully Made GET Request to /tasks")

 # making GET request to /tasks/id
Print("Making GET requests to /tasks/id ")
try:
	id = 1
	while id <= 10:
		url = address + "/tasks/%s" % id
		h = httplib2.Http()
		resp, result = h.request(url, 'GET')
		if resp['status'] != '200':
			raise Exception('Received an unsuccessful status code of %s' % resp['status'])
		id = id + 1
		
except Exception as err:
	print("Test 2 FAILED: Could not make GET Request to /tasks/id")
	print(err.args)
	sys.exit()
else:
	print("Test 2 PASS: Successfully made a GET Request to /tasks/id")

 
#Making a GET Request
print ("Making a GET Request for /tasks...")
try:
   url = address + "/tasks"
   h = httplib2.Http()
   resp, result = h.request(url, 'GET')
   if resp['status'] != '200':
      	raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
   print("Test 1 FAILED: Could not make GET Request to web server")
   print(err.args)
   sys.exit()
else:
   print("Test  PASS: Succesfully Made GET Request to /tasks")
   
 
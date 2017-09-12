import httplib2
import json
import sys

print("Running Endpoint Tester....\n ")
address = input("Enter the address of the server  \n Default: 'http://localhost:5000': ")
if address == '':
   address = 'http://localhost:5000'

   
#Making a GET Request
print ("Making a GET Request for /tasks...")
try:
   url = address + "/tasks"
   h = httplib2.Http()
   resp, result = h.request(url, 'GET')
   print ("GET resp =", resp)
   if resp['status'] != '200':
      	raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
   print("Test 1 FAILED: Could not make GET Request to web server")
   print(err.args)
   sys.exit()
else:
   print("Test 1  PASS: Succesfully Made GET Request to /tasks")
   
 
#Making a POST Request
print ("Making a POST Request for /tasks...")
try:
   url = address + "/tasks"
   h = httplib2.Http()
   resp, result = h.request(url, 'POST')
   print ("POST resp=", resp)
   if resp['status'] != '200':
      	raise Exception('Received an unsuccessful status code of %s' % resp['status'])
except Exception as err:
   print("Test 2 FAILED: Could not make POST Request to web server")
   print(err.args)
   sys.exit()
else:
   print("Test 2 PASS: Succesfully Made POST Request to /tasks")

 
# making GET request to /tasks/id
print("Making GET requests to /tasks/id ")
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
	print("Test 3 FAILED: Could not make GET Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 3 PASS: Successfully made a GET Request to /tasks/id")
	
   

	

 # making DELETE request to /tasks/id
print("Making GET requests to /tasks/id ")
try:
	id = 1
	while id <= 10:
		url = address + "/tasks/%s" % id
		h = httplib2.Http()
		resp, result = h.request(url, 'DELETE')
		if resp['status'] != '200':
			raise Exception('Received an unsuccessful status code of %s' % resp['status'])
		id = id + 1
		
except Exception as err:
	print("Test 5 FAILED: Could not make DELETE Request to web server")
	print(err.args)
	sys.exit()
else:
	print("Test 5 PASS: Successfully made a DELETE Request to /tasks/id")


# >>> from geocode import getGeocodeLocation
# >>> getGeocodeLocation("Turku,Finland")
# selaimesta : https://maps.googleapis.com/maps/api/geocode/json?
# address=Tampere+Finland&key=AIzaSyDviUUe100MfmNZsc4EInNH9d_1MbpeuUc
#
# use google maps to convert location into latitude/longitude coordinates
# format: 
# https://maps.googleapis.com/maps/api/geocode/json?address=Tampere+
# Finland&key=API_KEY

import httplib2
import json

def getGeocodeLocation(inputString):	
	google_api_key = "AIzaSyDviUUe100MfmNZsc4EInNH9d_1MbpeuUc"
	locationString = inputString.replace(" ","+")
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'%
	(locationString, google_api_key))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	latitude = result['results'][0]['geometry']['location']['lat']
	longitude = result['results'][0]['geometry']['location']['lng']
	return (latitude, longitude)
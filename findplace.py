from geocode import getGeocodeLocation
import json
import httplib2
 
# API Explorer
# https://api.foursquare.com/v2/venues/search?ll=40.7,-74 
# https://developer.foursquare.com/docs/explore#req=venues/search%3Fll%3D40.7,-74

# Create App: https://developer.foursquare.com/overview/auth -> register your app
# CLIENT_ID = JFUDJH1VBQI4LR5BO4505WVSF2L2NE5XUMUAORY2QFLO45MF
# CLIENT_SECRET = TUYHGXPYVR1MR0JPPAG4LSJPUTXVV3MTBX2F5SEQK1CN5PFR
# Application Url https://apicamp0/tamk.fi

# >>> from findplace import findPlace
# >>> findPlace("coffee","Helsinki")

fs_client_id = "JFUDJH1VBQI4LR5BO4505WVSF2L2NE5XUMUAORY2QFLO45MF"
fs_client_secret = "TUYHGXPYVR1MR0JPPAG4LSJPUTXVV3MTBX2F5SEQK1CN5PFR"

def findPlace(meal,location):
		# use getGeocodeLocation to get coordinates
		latitude, longitude = getGeocodeLocation(location)
		# use foursquore to find nearby restaurant
		url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20170214&ll=%s,%s&query=%s' % (fs_client_id, fs_client_secret,latitude,longitude,meal))
		h = httplib2.Http()
		result = json.loads(h.request(url, 'GET')[1])
		# get the 1st
		restaurant = result['response']['venues'][0]
		restaurant_name = restaurant['name']
		restaurant_address = restaurant ['location']['formattedAddress']
	#	restaurant_info
		result['response']['venues'][0]
		return (restaurant, restaurant_address)


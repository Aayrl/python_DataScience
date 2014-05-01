from urllib2 import urlopen
import json

# Latitude/Longitude grabber and Location Sniffer
# Based on http://stackoverflow.com/questions/20169467/how-to-convert-from-longitude-and-latitude-to-country-or-city
# Tyler J. Sawyer : 3/12/14

def getPlaceAtLatLon(lat, lon):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "latlng=%s,%s&sensor=false" % (lat, lon)
    v = urlopen(url).read()
    j = json.loads(v)
    address = j['results'][0]['formatted_address']
    return address

def getPlaceByName(name,state,country):
    url = "http://maps.googleapis.com/maps/api/geocode/json?"
    url += "address=%s,+%s,+%s&sensor=false" % (name,state,country)
    v = urlopen(url).read()
    j = json.loads(v)
    lat = j['results'][0]['geometry']['location']['lat']
    lon = j['results'][0]['geometry']['location']['lng']
    return lat, lon

print(getPlaceAtLatLon(44.475, -73.212))
print(getPlaceByName("Burlington","VT","USA"))
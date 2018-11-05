import requests
import json

possible_types = ["floods", "cyclones", "earthquakes"]
possible_alert_levels = ["green", "yellow", "orange", "red"]

#assign your google maps API key to this variable
api_key = ""

def long_lat(city):

    URL = "https://maps.googleapis.com/maps/api/geocode/json?address={}&key={api_key}".format(api_key=api_key)
    city = city.replace(" ", "+")
    URL = URL.format(city)
    r = requests.get(url = URL)

    #this is a dictionary
    data = r.json()
    return(data["results"][0]["geometry"]["location"])

def json_from_url(url):
    return requests.get(url).json()

#radius is in km, alert level is PAGER alert level
def dsearch(city=None, radius=None, alert_level = None, magnitude = None):
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query&format=geojson&limit=40"

    if city and radius:
        coordinates = long_lat(city)
        url += "&latitude=" + str(coordinates["lat"])
        url += "&longitude=" + str(coordinates["lng"])
        url += "&maxradiuskm=" + str(radius)

    if alert_level:
        if alert_level in possible_alert_levels:
            url += "&alertlevel=" + alert_level
        else:
            raise SyntaxError("alert_level isn't a possible alert level")

    if magnitude:
        url += "&minmagnitude=" + str(magnitude)

    print("Request made to: " + url)
    return json_from_url(url)

#test example
#print(json.dumps(dsearch(city="San Francisco", radius=500, magnitude=5)))

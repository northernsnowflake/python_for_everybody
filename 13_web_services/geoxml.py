# retrieves address, postal code and lon, lat information

import urllib.request, urllib.parse, urllib.error            
import xml.etree.ElementTree as ET 
import ssl


api_key = False
# if you have a google places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


#Ignore SSL certif. errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    results = tree.findall('result')
    lat = results['results'][0]['geometry']['location']['lat']
    lng = results['results'][0]['geometry']['location']['lng']
    location = results[0].find('formatted_address').text
    print('lat',lat,'lng', lng)
    print(location)

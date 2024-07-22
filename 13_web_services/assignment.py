import urllib.request, urllib.parse, urllib.error 
import xml.etree.ElementTree as ET
import ssl


'''
api_key = False
'''


counts = 0
sum = 0

"""
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
"""
#Ignore SSL certif. errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




stuff = input('Enter location: ')
html = urllib.request.urlopen(stuff, context=ctx).read()


tree = ET.fromstring(html) # retrieve url
lst = urllib.findall('.//count') # find all count

print('Count: ', len(lst))

for item in lst:
    number = item.text
    number = int(number)

    sum = sum + number

print('Sum',sum)
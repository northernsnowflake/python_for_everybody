# The program will prompt for URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from JSON data,compute the sum of the numbers in the file and enter the sum below:

import urllib.request, urllib.parse, urllib.error            
import json
import ssl


#Ignore SSL certif. errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sum = 0
url = input('Url')
html = urllib.request.urlopen(url, context = ctx).read()
info = json.loads(html)

print('Count: ', len(info['comments']))
comments = info['comments']
for item in comments:
    count = item['count']
    sum = sum + count 

print(sum)
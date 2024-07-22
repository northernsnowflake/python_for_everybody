import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # some special certificate
#Ignore SSL certif. errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ') # user insert url here 
html = urllib.request.urlopen(url, context=ctx).read() # URL
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
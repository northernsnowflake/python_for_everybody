from urllib.request import urlopen #import url open knihovny
from bs4 import BeautifulSoup # module to parse HTML
import ssl # some special certificate

#Ignore SSL certif. errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ') # user insert url here 
html = urlopen(url, context = ctx).read() #opens url, as a calling
soup = BeautifulSoup(html,'html.parser') #creates soup parser

#retrieve all the anchor tags
tags = soup('span')

for tag in tags:
    print('TAG:', tag)
    print('URL', tag.contents[0])
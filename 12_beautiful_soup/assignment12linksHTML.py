import urllib.request, urllib.parse, urllib.error 
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certif. errors

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)-1

i = 0
while i < count: #iterate pver the values per the user input
    html = urllib.request.urlopen(url, context = ctx).read() #opens url
    soup = BeautifulSoup(html,'html.parser') #creates soup parser
    tags = soup('a') # find out all a to later search for href (url)
    tag = tags[position] #we want only certain line
    url = tag.get('href', None) #find the url only, not the rest of messy line
    i = i + 1 #iterate
print(url)

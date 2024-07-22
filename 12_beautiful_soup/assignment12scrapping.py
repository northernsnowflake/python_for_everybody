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

# Retrieve all of the anchor tags
tags = soup('span') #list of all tags, but we want the group span only
count = 0
sum = 0
for tag in tags:
    value = tag.contents[0] # find the numbers in the table
    value = int(value) # convert to numbers
    count = count + 1 # count
    sum = sum + value # sum

print('Count', count)
print('Sum', sum)

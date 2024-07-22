import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
# open url, reads a data
for line in fhand: # iterate per each lines
    print(line.decode().strip()) #decode + strip 
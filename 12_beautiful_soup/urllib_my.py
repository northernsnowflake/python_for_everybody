import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# open url, reads a data
for line in fhand: # iterate per each lines
    print(line.decode().strip()) #decode + strip 
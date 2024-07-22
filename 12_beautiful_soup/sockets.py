# Program that reads the HTTP that opens socket, sends a command and retrieves a data - and geths its header and content

import socket

# open socket 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #make a socket - file handler without data 
# connect data to the socket, single tuple as parameter0 and parameter1 (as port 80)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode() #HTTP + end of line + new line
# encode to bytes

# send as command
mysock.send(cmd) # send data

# retrieve the data
while True: # simple while loop up to 512 characters
    data = mysock.recv(512) #UTF 8
    if (len(data) < 1): #if there is end of file
        break
    print(data.decode()) #decode it to unicode
mysock.close()

        


import socket 

while True:
    data = mysock.recv(512) #bytes  ## 1 bit = 4bytes
    if (len(data) < 1): 
        break
    mystring = data.decode() #UTF-8
    print(mystring)
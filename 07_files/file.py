xfile = open('mbox.txt','r')
count = 0

for line in xfile:
    count = count + 1
print('There is', count, 'lines in file')
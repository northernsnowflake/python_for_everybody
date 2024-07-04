fname = input('Enter filename: ')

try:
    fhand = open(fname, 'r')
except:
    print('File cannot be opened:',fname)
    quit()

count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith("Subject: "):
        count = count + 1
print('There were',count, 'subject lines in', fname)


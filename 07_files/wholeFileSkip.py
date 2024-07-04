fhand = open('mbox-short.txt', 'r') #reads file

# Search operation in file - prints all from line
for line in fhand:
    line = line.rstrip() # strip space in the end
    if not line.startswith('From:'):
        continue
    print(line)
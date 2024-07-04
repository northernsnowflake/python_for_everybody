fhand = open('mbox-short.txt', 'r') #reads file

# Search operation in file - all lines where is not @uct.ac.za skips
for line in fhand:
    line = line.rstrip() # strip space in the end
    if not '@uct.ac.za' in line:
        continue
    print(line)
#finds which days someone write me and email

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])

line = 'From stephen.marquart@uct.ac.za Sat Jan  5 09:14:16 2008'
words = line.split()
print(words)
fhand = open("mbox-short.txt")

counts = dict()

for line in fhand: 
    if line.startswith("From "): # vezmi vsechny zacinajici From
        words = line.strip('\n') # do konce radku
        splitted = words.split() # rozdel na slova
        date = splitted[5]
        hours = date.split(':') #vse mezi:
        
        h = hours[0]

        counts[h] = counts.get(h,0) + 1 # for histogram 

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)

for val, key in lst[:12]:
    print(val, key)

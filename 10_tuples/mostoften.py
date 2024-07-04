fhand = open('romeo.txt') # opening the file
counts = dict()  # make a dictionary


for line in fhand: # loop through lines of the file
    words = line.split() # split words in the file -- -- --
    for word in words: # loop through the each word
        counts[word] = counts.get(word, 0) + 1 # loop through the files, must be same on the left and right side as in chemistry
            # creates the histograms of the most often data
#print(words)
#print(counts)

lst = list()
for key, val in counts.items():
    newtup = (val,key)
    lst.append(newtup) # append it to the newtup
        #list of tuples in val, key order 29, tree


print(lst)
# seradte to od nejvyssi do nejnizsi REVERSE
lst = sorted(lst,reverse = True) # highest to lowest

print(lst)
# (v,k)
for val, key in lst[:10]:
    print(key,val) # flipping the order 

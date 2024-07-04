fname = input('Enter file: ')
if len(fname) < 1: fname = 'mbox-short.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip() #open the lines
    #print(lin)
    wds = lin.split() #split into the lines
    print(wds)
    for w in wds:
        # if the key is not there the count is zero
        di[w] = di.get(w,0) + 1 


print(di)

largest = -1
k = None
v = None

for k,v in di.items():
    if v > largest:
        largest = 0
        theword = k 
print(theword,largest)

# Use the file name mbox-short.txt as the file namemb

fname = input("Enter file name: ")

count = 0
size = 0

fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    a = int(line.find(':'))
    b = line[a+2:]
    b = float(b)

    count = count+1 # kolik jich tam je
    size = size + b # secti je radek po radku, vzdy pricti to cislo
    #print(count,b)

#print(count)
#print(size)
print("Average spam confidence: ", size/count)
# use 07/words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File can not be opened: ', fname)

a = fh.read()
for line in a:
    line = line.rstrip() # avaid the newlines
    b = a.upper()
print(b)
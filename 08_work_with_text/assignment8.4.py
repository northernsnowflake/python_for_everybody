flat = []
fname = input("Enter file name: ")
fh = open(fname)

a =[]

for line in fh:
    line = line.rstrip() #odstrani mezery
    words = line.split() #rozdeli na radky

    a.append(words)

for i in a:
    flat+=i


flat.remove('and')
flat.remove('and')
flat.remove('is')
flat.remove('is')
#flat.remove('sun')
flat.remove('the')
flat.remove('the')
#flat.sort()
print(flat)
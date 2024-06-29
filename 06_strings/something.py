greet = 'Hello Bob      '
zap = greet.lower() #make a copy of lowercase
print(zap)
print(greet)

pos = greet.find('llo')
print(pos)

nstr = greet.replace('Bob','Kate')
print(nstr)

nstr2 = greet.replace('o','XXX')
print(nstr2)

strip1 = greet.strip()
print(strip1)

str2 = greet.startswith('Please') # gives true or false
print(str2)